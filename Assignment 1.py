# Jacob Delgado
# Assignment 1
import math
import sys
import re
from queue import Queue

totalCost = 0
# Dictionaries for nodes
nodeLocation = {}
radnodeLocation = {}
# Dictionary for map distances
nearbyLocation = {}
# Dictionary for straight lines distances to their neighbors
lineDistance = {}

class NodePivot:
    def __init__(self, currentData):
        self.items = currentData
        self.distance = math.inf
        self.currentScore = math.inf
        self.neighbors = []
        self.previousLocation = None

    def __str__(self):
        return self.items

    def getItems(self):
        return self.items

    def getNearbyCities(self):
        return self.neighbors

    def getDistance(self):
        return self.distance

    def setDistance(self, d):
        self.distance = d

    def newNeighbors(self, near):
        self.neighbors.append(near)


def ConvertToRad(value):
    radValue = (math.radians(value))  # Based on formula given
    return radValue

def LineDistance(lat1, lat2, long1, long2):
    r = 3958.8
    latitude = math.pow(math.sin((lat2-lat1)/2), 2)
    longitude = math.pow(math.sin((long2-long1)/2), 2)
    co = math.cos(lat1)*math.cos(lat2)*longitude
    d = (2*r*math.asin(math.sqrt(latitude + co)))
    return d

def cityDistancesToEnd(StartCity, EndCity):
    # import global total cost
    global totalCost
    global radnodeLocation
    global nearbyLocation
    global lineDistance

    # print(radnodeLocation[EndCity])

    # Calculate initial distance length from given start to end
    line = LineDistance(radnodeLocation[StartCity][0], radnodeLocation[EndCity][0], radnodeLocation[StartCity][1],
                         radnodeLocation[EndCity][1])

    # print(line)
    # Create merged string for straight line distances
    cityDist = StartCity
    lineDistance[cityDist] = line
    # Loop through all cities with coordinates
    for i in radnodeLocation:
        # Calculate line distance so long as it's not the start city
        if i != StartCity:
            # Create merged string for straight line distances
            cityDist2 = i
            # Get line distance
            distances = LineDistance(radnodeLocation[i][0], radnodeLocation[EndCity][0],
                                 radnodeLocation[i][1], radnodeLocation[EndCity][1])
            # Add line distance to dictionary
            lineDistance[cityDist2] = distances
    # print(lineDistance)

# Create a queue by using matching dictionary values to get the proper distances
def bestDistance(StartCity):
    # import global total cost
    global totalCost
    global nodeLocation
    global radnodeLocation
    global nearbyLocation
    global lineDistance
    # print(lineDistance)

    totalCost = 0
    # Set the score of the first node to the direct line distance to destination
    startDist = lineDistance[StartCity]
    # print(startDist)

    previousLocation = StartCity
    # print(previousLocation)
    # print(type(previousLocation))
    mapQ = Queue()
    mapQ.put(StartCity)
    # print(StartCity)

    while mapQ.qsize() > 0:
        currentCity = mapQ.get()

        # print(nearbyLocation[currentCity.getItems()])
        # print(current_v)
        print(previousLocation)
        print(type(previousLocation))

        count = 0
        # mapQ.put(nearbyLocation[currentCity.getItems()][0])
        # Iterate the neighbor list of the current vertex
        for n in nearbyLocation[currentCity]:
            # print(n)
            # print(type(n))
            if count > len(nearbyLocation[currentCity]):
                break
            if n != previousLocation:
                count += 2
                if count > len(nearbyLocation[currentCity]):
                    break
                else:
                    # print(nearbyLocation)
                    nearby = nearbyLocation[currentCity][count]
                    # print(nearby)
                    # print(type(nearby))
                    mapQ.put(nearby)
                    # print(n)

            # Calculate the distance from current to reach n + current distance + from n to endpoint
            astar_score = nearbyLocation[nearby] + totalCost + lineDistance[currentCity]
        # print(mapQ)

def ProgramInput(inputs):
    # import global total cost
    global totalCost
    global nodeLocation
    global radnodeLocation
    global nearbyLocation
    # Grab start and end city from user input
    StartCity, EndCity = inputs.strip().split()
    # Display inputs
    # print(f'From city: {StartCity}')
    # print(f'To city: {EndCity}')
    # Find text files containing map and node data
    node_path = 'coordinates.txt'
    map_path = 'map.txt'

    # out = open("output.txt", "w")
    with open(node_path, 'r') as coord:
        for line in coord.readlines():
            n = line.strip().replace('(', '').replace(')', '').split(':')
            latitude, longitude = n[1].split(',')
            radLat = ConvertToRad(float(latitude))
            radLong = ConvertToRad(float(longitude))
            city = n[0]
            # coordinates = radLong
            # nodeLocation[city] = latitude, longitude # Test if
            radnodeLocation[city] = radLat, radLong
            # print(LineDistance())
            # print(n[0])
            # print(n[1])
    # print(radnodeLocation["SanJose"][0])
    #Close the file
    coord.close()

    # Grab all city names to turn into NodePivot objects
    nodeKeys = radnodeLocation.keys()

    # list for holding city pivot names
    cities = []
    # Loop through the cities
    for x in nodeKeys:
        # Add cities to list as pivot object
        cities.append(NodePivot(x))

    # Loop through city list
    for i in cities:
        # When the starting city is found, set it as the starting pivot
        if StartCity == i.items:
            # Assign starting pivot
            cityPivot = i
        if EndCity == i.items:
            # Assign ending pivot object
            pivotEnd = i

    # print(cityPivot)
    # print(cities)


    # Open map file
    with open(map_path, 'r') as map:
        # Loop through file lines
        for line in map.readlines():
            # Split from starting location
            m = line.strip().split('-')
            # Assign value for start city
            mapCity = m[0]
            # Split rest of nearby cities
            nearCity = m[1].split(',')
            # Split nearby cities and their distances
            nCity = nearCity[0].replace(')', '').split('(')
            # print(f'nearCity[0] is {nCity}')
            # Create dictionary with start city - next city as key with their distances as values as tuples
            nearbyLocation[mapCity] = nCity[0], float(nCity[1])
            # print(nearbyLocation[mapCity][0])
            # print(i)
            # Loop through the rest of the nearby cities
            for f in range(1, len(nearCity)):
                # Split values
                nCity2 = nearCity[f].replace(')', '').split('(')
                # Add merged cities and their map given distance
                nearbyLocation[mapCity] += nCity2[0], float(nCity2[1])
            # print(type(nearbyLocation[cityMerge]))
            # print(nearbyLocation)
            # print(cityMerge)
            # print(nearCity)
            # print(nCity)
            # print(nCity2)
            # print(nearbyLocation)
        # print(nearbyLocation[StartCity][0][1])
    # Close the file
    map.close()
    # Test LineDistance formula
    # e = LineDistance(radnodeLocation[StartCity][0],radnodeLocation[EndCity][0],radnodeLocation[StartCity][1],radnodeLocation[EndCity][1])
    # print(e)
    # print(nodeLocation)
    # print(nearbyLocation[StartCity][0])
    # print(radnodeLocation)

    # Create dictionary for all cities towards endpoint
    cityDistancesToEnd(StartCity, EndCity)
    # Find the best route to the endpoint
    bestDistance(StartCity)


ProgramInput('Monterey SanDiego')

