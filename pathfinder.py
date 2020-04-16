from geodata import *

fake_location0 = Location(0, "location 0", 0.0005, 0.0005, 5)
fake_location1 = Location(1, "location 1", 0.001, 0.001, 10)
fake_location2 = Location(2, "location 2", 0.0015, 0.0015, 15)
fake_locations = [fake_location0, fake_location1, fake_location2]

locations = fake_locations
streets = [Street(0, "street 0", fake_locations)]
start = fake_locations[0]
end = fake_locations[2]
shortest_distance = 0
shortest_path = []
min_ele_distance = 0
min_ele_gain = 0
min_ele_path = []
max_ele_distance = 0
max_ele_gain = 0
max_ele_path = []

graph = Graph(locations, streets)
graph.initialization()
shortest_path = graph.short_path(start, end, shortest_distance)
min_ele_path = graph.min_ele_path(start, end, min_ele_distance, min_ele_gain)
max_ele_path = graph.max_ele_path(start, end, max_ele_distance, max_ele_gain)
print()
for vertex in shortest_path:
	print(vertex.locid, vertex.name)
print()
for vertex in min_ele_path:
	print(vertex.locid, vertex.name)
print()
for vertex in max_ele_path:
	print(vertex.locid, vertex.name)