import sys
from collections import defaultdict
import re


class Edge:
    def __init__(self, _begin, _end, _distance):
        self.being = _begin
        self.end = _end
        self.distance = _distance

    def __str__(self):
        return self.begin + ", " + self.end + ", " + str(self.distance)


class Nodes:
    def __init__(self):
        self.graph = defaultdict(list)  # dictionary that holds all connected key and edges to the list

    def add_edge(self, key, _edge):
        self.graph[key].append(_edge)


class Route:
    def __init__(self):
        self.path = list()
        self.travelled = 0


def copy_route(_route):
    new_r = Route()
    new_r.path = _route.path.copy()
    new_r.travelled = _route.travelled
    return new_r


def travel(_paths, _nodes, _city, _route):
    # get all destinations one can travel to from this city
    _route.path.append(_city.end)
    _route.travelled += _city.distance

    next_city: Edge
    for next_city in _nodes.graph.get(_city.end):
        if next_city.end in _route.path:
            continue
        else:
            next_route = copy_route(_route)
            travel(_paths, _nodes, next_city, next_route)

    # if route covered all cities then add it to the path
    if len(_route.path) == len(_nodes.graph):
        _paths.append(_route)



instructions = open('2015Day9.txt')
#instructions = open('test.txt')
nodes = Nodes()
for line in instructions:
    line = line.rstrip()
    line = re.sub(r"(\sto\s|\s=\s)", ",", line)
    begin, end, distance = re.split(",", line)
    nodes.add_edge(begin, Edge(begin, end, int(distance)))
    nodes.add_edge(end, Edge(end, begin, int(distance)))


paths = list()
for starting_city in nodes.graph: # all routes (different starting point)
    destination: Edge
    for destination in nodes.graph.get(starting_city):
        route = Route()
        route.path.append(destination.being)
        travel (paths, nodes, destination, route)


shortest_distance = sys.maxsize
longest_distance = 0
shortest_path = None
longest_distancelongest_path = None
k: Route
for k in paths:
    #print("path = " + k.path.__str__() + " distance = " + str(k.travelled))
    if shortest_distance > k.travelled:
        shortest_distance = k.travelled
        shortest_path = k.path
    if longest_distance < k.travelled:
        longest_distance = k.travelled
        longest_path = k.path


print("shortest path = " + shortest_path.__str__() + " distance = " + str(shortest_distance))
print("longest path = " + longest_path.__str__() + " distance = " + str(longest_distance))
