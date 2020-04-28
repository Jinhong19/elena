from server import Place
from server import Intersection

places = Place.query.all()

for e in places: 
    print(e.name, e.ele, e.lon)

intersections = Intersection.query.all()

for e in intersections: 
    print(e)