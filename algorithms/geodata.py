from math import sin, cos, sqrt, atan2, radians
import sys

class Location:
	def __init__(self, locid, name, lat, lon, ele, street):
		self.locid = locid
		self.name = name
		self.lat = lat
		self.lon = lon
		self.ele = ele
		self.street = street

	def to_json(self):
		return {"id": self.locid, "name": self.name, "lat": self.lat, "lon": self.lon, "ele": self.ele}

class Graph:
	def __init__(self, locations, streets, intersections):
		self.locations = locations
		self.streets = streets
		self.graph_dict = {}
		self.all_path = []
		self.intersections = intersections

	def get_distance(self, location1, location2):
		R = 6373

		lat1 = radians(location1.lat)
		lon1 = radians(location1.lon)
		lat2 = radians(location2.lat)
		lon2 = radians(location2.lon)

		dlon = lon2 - lon1
		dlat = lat2 - lat1

		a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
		c = 2 * atan2(sqrt(a), sqrt(1 - a))
		distance = R * c
		#The distance is in km
		return distance

	def link(self, location1, location2):
		distance = self.get_distance(location1, location2)
		ele_change = location2.ele - location1.ele
		if location1 in self.graph_dict:
			self.graph_dict[location1].append((location2, distance, ele_change))
		else:
			self.graph_dict[location1] = [(location2, distance, ele_change)]
		if location2 in self.graph_dict:
			self.graph_dict[location2].append((location1, distance, -ele_change))
		else:
			self.graph_dict[location2] = [(location1, distance, -ele_change)]

	def add_location(self, location):
		if location not in self.graph_dict:
			self.graph_dict[location] = []

	def add_street(self, street):
		temp_locations = []
		for sp in street:
			temp_locations.append(sp)
		if len(temp_locations) < 2:
			return
		center = Location(-1, "temp_center", 0, 0, 0, "")
		for sp in temp_locations:
			center.lat = center.lat + sp.lat
			center.lon = center.lon + sp.lon
		center.lat = center.lat / len(temp_locations)
		center.lon = center.lon / len(temp_locations)
		edge = center
		edge_distance = 0
		for sp in temp_locations:
			if self.get_distance(center, sp) > edge_distance:
				edge_distance = self.get_distance(center, sp)
				edge = sp

		temp_locations.remove(edge)
		while len(temp_locations) > 0:
			close = temp_locations[0]
			close_distance = self.get_distance(edge, temp_locations[0])
			for sp in temp_locations:
				if self.get_distance(edge, sp) < close_distance:
					close_distance = self.get_distance(edge, sp)
					close = sp
			ele_change = close.ele - edge.ele
			self.link(edge, close)
			edge = close
			temp_locations.remove(close)

	def add_intersection(self, intersection):
		st1 = intersection.firstStreet
		st2 = intersection.secondStreet
		if st1 not in self.streets or st2 not in self.streets:
			print("Error: Street in intersection not found")
			return

		close1 = self.streets[st1][0]
		close2 = self.streets[st2][0]
		center = Location(-1, "temp_center", intersection.lat, intersection.lon, 0, "")
		close_distance1 = self.get_distance(center, close1)
		close_distance2 = self.get_distance(center, close2)
		for sp in self.streets[st1]:
			if self.get_distance(sp, center) < close_distance1:
				close_distance1 = self.get_distance(sp, center)
				close1 = sp
		for sp in self.streets[st2]:
			if self.get_distance(sp, center) < close_distance2:
				close_distance2 = self.get_distance(sp, center)
				close2 = sp
		self.link(close1, close2)

	def initialization(self):
		for location in self.locations:
			self.add_location(location)

		for street in self.streets:
			self.add_street(self.streets[street])

		for it in self.intersections:
			self.add_intersection(it)

	#Using Dijkstra algorithm for shortest path
	def short_path(self, start, end):
		distance = 0
		solution = []
		q = []
		dist = {}
		prev = {}

		for vertex in self.locations:
			dist[vertex] = sys.maxsize
			prev[vertex] = None
			q = q + [vertex]
		dist[start] = 0

		while len(q) != 0:
			current_min = sys.maxsize
			target_min = None
			for vertex in q:
				if dist[vertex] < current_min:
					current_min = dist[vertex]
					target_min = vertex

			if(target_min == None):
				print("Error: Map not connected")
				return
			
			q.remove(target_min)
			if target_min == end:
				distance = dist[end]
				temp = end
				while temp != None:
					solution.insert(0, temp)
					temp = prev[temp]
				return solution, distance

			for path in self.graph_dict[target_min]:
				if path[0] in q:
					alt = dist[target_min] + path[1]
					if alt < dist[path[0]]:
						dist[path[0]] = alt
						prev[path[0]] = target_min
		return solution, distance

	#Using Dijkstra algorithm for min ele gain path
	#Find the min ele gain for sure without the length limit
	def min_ele_dijk(self, start, end, distance, total_ele_gain):
		distance = 0
		total_ele_gain = 0
		solution = []
		q = []
		ele_gain = {}
		prev = {}
		distance = {}

		for vertex in self.locations:
			ele_gain[vertex] = sys.maxsize
			prev[vertex] = None
			q = q + [vertex]
		ele_gain[start] = 0
		distance[start] = 0

		while len(q) != 0:
			current_min = sys.maxsize
			target_min = None
			for vertex in q:
				if ele_gain[vertex] < current_min:
					current_min = ele_gain[vertex]
					target_min = vertex
			q.remove(target_min)
			if target_min == end:
				distance = distance[end]
				total_ele_gain = ele_gain[end]
				temp = end
				while temp != None:
					solution.insert(0, temp)
					temp = prev[temp]
				return solution

			for path in self.graph_dict[target_min]:
				if path[0] in q:
					alt = ele_gain[target_min]
					if path[2] > 0:
						alt = alt + path[2]
					if alt < ele_gain[path[0]]:
						ele_gain[path[0]] = alt
						prev[path[0]] = target_min
						distance[path[0]] = distance[target_min] + path[1]

		return solution

	#Using Dijkstra algorithm for max ele gain path
	#Find the max ele gain for sure without the length limit
	def max_ele_dijk(self, start, end, distance, total_ele_gain):
		distance = 0
		total_ele_gain = 0
		solution = []
		q = []
		ele_gain = {}
		prev = {}
		distance = {}

		for vertex in self.locations:
			ele_gain[vertex] = -2
			prev[vertex] = None
			q = q + [vertex]
		ele_gain[start] = 0
		distance[start] = 0

		while len(q) != 0:
			current_max = -1
			target_max = None
			for vertex in q:
				if ele_gain[vertex] > current_max:
					current_max = ele_gain[vertex]
					target_max = vertex
			q.remove(target_max)
			if target_max == end:
				distance = distance[end]
				total_ele_gain = ele_gain[end]
				temp = end
				while temp != None:
					solution.insert(0, temp)
					temp = prev[temp]
				return solution

			for path in self.graph_dict[target_max]:
				if path[0] in q:
					alt = ele_gain[target_max]
					if path[2] > 0:
						alt = alt + path[2]
					if alt > ele_gain[path[0]]:
						ele_gain[path[0]] = alt
						prev[path[0]] = target_max
						distance[path[0]] = distance[target_max] + path[1]

		return solution

	#Using BFS with length limit for all paths
	#Find all paths from start to end within the length limit

	def bfs_helper(self, u, d, visited, path, current_distance, distance_limit, current_ele_gain):
		visited[u] = True
		path.append(u)

		if u == d:
			temp = []
			for i in path:
				temp.append(i)
			self.all_path.append((temp, current_distance, current_ele_gain))
		else:
			for i in self.graph_dict[u]:
				if visited[i[0]] == False:
					if current_distance + i[1] <= distance_limit:
						ele_gain = 0
						if i[2] > 0:
							ele_gain = i[2]
						self.bfs_helper(i[0], d, visited, path, current_distance + i[1], distance_limit, current_ele_gain + ele_gain)

		path.pop()
		visited[u] = False

	def bfs(self, s, d, distance_limit):
		visited = {}
		for vertex in self.locations:
			visited[vertex] = False

		path = []
		current_distance = 0
		current_ele_gain = 0
		self.bfs_helper(s, d, visited, path, current_distance, distance_limit, current_ele_gain)