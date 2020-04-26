from server import db
from server import Place
from eleFinder import eleFinder
from OSMPythonTools.overpass import Overpass, overpassQueryBuilder

overpass = Overpass()
eleFinder = eleFinder()

db.create_all()

# Geodata Query
area = [42.351000, -71.063000, 42.353000, -71.061000] # boston

# insert into database
def query():
    # find places in bbox that have name and street name
    query = overpassQueryBuilder(bbox=area, elementType='node', selector=[
                             'name', '"addr:street"'])
    result = overpass.query(query)
    elements = result.elements()
    for e in elements:
        print(e.tags())
        # find elevation
        ele = eleFinder.getEle(e.lat(), e.lon())
        # create place object
        street = e.tag('addr:street')
        place = Place(id=e.id(), name=e.tag('name'), lat=e.lat(),
                      lon=e.lon(), ele=ele, street=street)
        db.session.add(place)
    db.session.commit()


# query()