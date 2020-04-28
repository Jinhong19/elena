import sys
import os
sys.path.insert(1, os.path.abspath("BackEnd"))
from eleFinder import *
from server import Place
from server import Intersection

places = Place.query.all()

for e in places: 
    print(e.name, e.ele, e.lon)

intersections = Intersection.query.all()

for e in intersections: 
    print(e)

eleFinder = eleFinder()

def test_getEle1():
    assert round(eleFinder.getEle(42.36003, -71.05515), 2) == 2.73

def test_getEle2():
    assert round(eleFinder.getEle(42.36124, -71.04916), 2) == -2.10

def test_getEle3():
    assert round(eleFinder.getEle(42.35800, -71.05776), 2) == 8.38

test_getEle1()
test_getEle2()
test_getEle3()