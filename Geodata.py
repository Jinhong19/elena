from math import sin, cos, sqrt, atan2, radians

class Location:
	def __init__(self, locid, name, lat, lon, ele):
		self.locid = locid
		self.name = name
		self.lat = lat
		self.lon = lon
		self.ele = ele

class Street:
	def __init__(self, stid, name, listOfLocations):
		self.stid = stid
		self.name = name
		self.listOfLocations = listOfLocations

class Graph:
	def __init__(self, locations, streets):
		self.locations = locations
		self.streets = streets
		self.graph_dict = {}

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

	def add_location(self, location):
		if location not in self.graph_dict:
			self.graph_dict[location] = []

	def add_street(self, street):
		locations = street.listOfLocations
		if len(locations) > 1:
			for i in range(len(locations))-1:
				distance = get_distance(locations[i], locations[i+1])
				if(locations[i] in self.graph_dict):
					self.graph_dict[locations[i]].append((locations[i+1], distance))
				else:
					self.graph_dict[locations[i]] = [(locations[i+1], distance)]
				if(locations[i+1] in self.graph_dict):
					self.graph_dict[locations[i+1]].append((locations[i], distance))
				else:
					self.graph_dict[locations[i+1]] = [(locations[i], distance)]

	def initialization(self):
		for location in self.locations:
			add_location(location)
		for street in self.streets:
			add_street(street)