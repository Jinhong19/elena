from BackEnd import eleFinder

eleFinder = eleFinder()

def test_getEle1():
    assert eleFinder.getEle(42.360033, -71.055147) == 11

def test_getEle2():
    assert eleFinder.getEle(42.361238, -71.049158) == -2

def test_getEle3():
    assert eleFinder.getEle(42.358004, -71.057745) == 132