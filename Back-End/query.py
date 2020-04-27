from server import db
from server import Place
from server import Intersection
from eleFinder import eleFinder
from OSMPythonTools.overpass import Overpass, overpassQueryBuilder

overpass = Overpass()
eleFinder = eleFinder()

try:
    Place.query.all()
except:
    db.create_all() 
    print("database created")


# Geodata Query
# area = [south, west, north, east]
bostonArea = [42.330022,-71.093372,42.365393,-71.036305]
amherstArea = [42.371082, -72.538644, 42.395476, -72.499210]
smallBostonArea = [42.346968,-71.064661,42.361969,-71.052636]
area = amherstArea


# insert into database
def queryPlaces():
    # find places in bbox that have name and street name
    query = overpassQueryBuilder(bbox=area, elementType='node', selector=[
                             'name', '"addr:street"'])
    result = overpass.query(query)
    elements = result.elements()
    print ("Ran query with " + query)
    for e in elements:
        print(e.tags())
        # find elevation
        ele = eleFinder.getEle(e.lat(), e.lon())
        # create place object
        street = e.tag('addr:street')
        print(ele)
        place = Place(id=e.id(), name=e.tag('name'), lat=e.lat(),
                      lon=e.lon(), ele=ele, street=street)
        db.session.add(place)
    db.session.commit()

areaString = ",".join([str(a) for a in area])
def overpassIntersectionString(s1, s2):
    return 'way[highway][name="{}"]({})->.w1;way[highway][name="{}"]({})->.w2;node(w.w1)(w.w2);out;'.format(s1, areaString, s2, areaString)

def queryIntersections():
    data = Place.query.all()

    # get all streets
    streets = set()
    for p in data:
        if p.street not in streets:
            streets.add(p.street)

    # build a list of query
    queryList = [{'s1': s1, 's2': s2, 'query': overpassIntersectionString(s1, s2)} for s1 in streets for s2 in streets if s1 != s2]
    print(len(queryList))
    # print(queryList[0])

    # run the query and store intersections in database
    for streetPair in queryList:
        query = streetPair['query']
        result = overpass.query(query)
        elements = result.elements()
        if len(elements) > 0:
            e = elements[0]
            intersection = Intersection(lat=e.lat(), lon=e.lon(), firstStreet=streetPair['s1'], secondStreet=streetPair['s2'])
            print(intersection)
            db.session.add(intersection)
    db.session.commit()
