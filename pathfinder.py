from Geodata import *
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


fake_location0 = Location(0, "location 0", 0.0005, 0.0005, 5)
fake_location1 = Location(1, "location 1", 0.001, 0.001, 10)
fake_location2 = Location(2, "location 2", 0.0015, 0.0015, 15)
fake_location3 = Location(3, "location 3", 0.002, 0.002, 20)
fake_locations = [fake_location0, fake_location1, fake_location2, fake_location3]
fake_locations0 = [fake_location0, fake_location1]
fake_locations1 = [fake_location0, fake_location3]
fake_locations2 = [fake_location1, fake_location2]
fake_locations3 = [fake_location2, fake_location3]

locations = fake_locations
streets = [Street(0, "street 0", fake_locations0), Street(1, "street 1", fake_locations1), Street(2, "street 2", fake_locations2), Street(3, "street 3", fake_locations3)]
start = fake_locations[0]
end = fake_locations[2]
shortest_distance = 0
distance_limit = 0
shortest_path = []

graph = Graph(locations, streets)
graph.initialization()
shortest_path, shortest_distance = graph.short_path(start, end)
distance_limit = shortest_distance * 3

graph.bfs(start, end, distance_limit)

json_output = {
  "start_point": start.to_json(),
  "end_point": end.to_json(),
  "shortest_distance": shortest_distance,
  "shortest_path": path_to_json(shortest_path),
  "all_path": all_path_to_json(graph.all_path)
}

with open('data.json', 'w', encoding='utf-8') as f:
	json.dump(json_output, f, ensure_ascii=False, indent=4)