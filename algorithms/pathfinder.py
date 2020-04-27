import sys
import os
print(os.path.abspath("../Back-End"))
sys.path.insert(1, os.path.abspath("../Back-End"))
#from server import Place
from geodata import *
import json

def path_to_json(path):
	json_list = []
	for i in path:
		json_list.append(i.to_json())
	return json_list

def all_path_to_json(all_path):
	json_list = []
	for i in all_path:
		json_list.append({"distance": i[1], "ele_gain": i[2], "path": path_to_json(i[0])})
	return json_list

def main_controller(start, end, percent):

	location0 = Location(0, "location0", 0.0001, 0.0001, 1, "street0")
	location1 = Location(1, "location1", 0.0002, 0.0002, 2, "street0")
	location2 = Location(2, "location2", 0.0003, 0.0003, 3, "street0")
	location3 = Location(3, "location3", 0.0004, 0.0004, 4, "street0")
	location4 = Location(4, "location4", 0.0005, 0.0005, 5, "street0")
	locations = [location0, location1, location2, location3, location4]

#	data = Place.query.all()
#	locations = []
#	for sp in data:
#		locations.append(Location(sp.id, sp.name, sp.lat, sp.lon, sp.ele, sp.street))
	streets = {}
	for sp in locations:
		if sp.street in streets:
			streets[sp.street].append(sp)
		else:
			streets[sp.street] = [sp]


	graph = Graph(locations, streets)
	graph.initialization()
	
	for sp in graph.graph_dict:
		print("location name:")
		print(sp.name)
		print("connected to:")
		for data in graph.graph_dict[sp]:
			print(data[0].name)
			print(data[1])
			print(data[2])
		print("--------------")
	
	start_point = None
	end_point = None
	for sp in graph.locations:
		if sp.name == start:
			start_point = sp
		elif sp.name == end:
			end_point = sp
	if start_point == None:
		print("Error: Start point not found")
		return
	elif end_point == None:
		print("Error: End point not found")
		return
	shortest_distance = 0
	distance_limit = 0
	shortest_path = []
	shortest_path, shortest_distance = graph.short_path(start_point, end_point)
	distance_limit = shortest_distance * percent
	graph.bfs(start_point, end_point, distance_limit)
	json_output = {
	  "start_point": start_point.to_json(),
	  "end_point": end_point.to_json(),
	  "shortest_distance": shortest_distance,
	  "shortest_path": path_to_json(shortest_path),
	  "all_path": all_path_to_json(graph.all_path)
	}
	print(json.dumps(json_output, indent=4))

main_controller("location0", "location4", 3.0)