from server import Place

data = Place.query.all()

for sp in data: 
    print(sp.name, sp.ele, sp.lon)