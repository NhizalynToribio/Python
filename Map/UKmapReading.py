print("**************** PROGRAMMED BY: *****************")
print("************** NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("**Python Stacks, Queues, and Priority Queues **")
print("*************** UK Map Reading Files *******************")


import networkx as nx
from graph import (
    City,
    load_graph,
    breadth_first_traverse,
    breadth_first_search as bfs,
    shortest_path,
    connected,
    depth_first_traverse,
    depth_first_search as dfs,
    dijkstra_shortest_path
)


print("First Testing: Using networkx module:")
nodes, graph = load_graph("roadmap.dot", City.from_dict)

print(nodes["london"])
print("\n")
print(graph)


print("\n2nd testing")
for neighbor in graph.neighbors(nodes["london"]):
    print(neighbor.name)


print("\n3rd testing")
for neighbor, weights in graph[nodes["london"]].items():
    print(weights["distance"], neighbor.name)


print("\n4th testing")


def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))


def by_distance(weights):
    return float(weights["distance"])


for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
    print(f"{weights['distance']:>3} miles, {neighbor.name}")


print("\n5th testing")


def is_twentieth_century(year):
    return year and 1901 <= year <= 2000


nodes, graph = load_graph("roadmap.dot", City.from_dict)
for node in nx.bfs_tree(graph, nodes["edinburgh"]):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
else:
    print("Not found")


print("\n6th testing")


def order(neighbors):
    def by_latitude(city):
        return city.latitude
    return iter(sorted(neighbors, key=by_latitude, reverse=True))


for node in nx.bfs_tree(graph, nodes["edinburgh"], sort_neighbors=order):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
else:
    print("Not found")

# Testing the breadth-first search and traversal implementations
print("\n7th testing")


def is_twentieth_century(city):
    return city.year and 1901 <= city.year <= 2000


nodes, graph = load_graph("roadmap.dot", City.from_dict)
city = bfs(graph, nodes["edinburgh"], is_twentieth_century)
print(city.name)
print("\n")
for city in breadth_first_traverse(graph, nodes["edinburgh"]):
    print(city.name)


print("\n8th testing")
nodes, graph = load_graph("roadmap.dot", City.from_dict)

city1 = nodes["aberdeen"]
city2 = nodes["perth"]

for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1):
    print(f"{i}.", " → ".join(city.name for city in path))


print("\n9th testing")
print(" → ".join(city.name for city in shortest_path(graph, city1, city2)))


def by_latitude(city):
    return -city.latitude


print(" → ".join(
    city.name
    for city in shortest_path(graph, city1, city2, by_latitude)
))

print("\n10th testing")
print(connected(graph, nodes["belfast"], nodes["glasgow"]))

print(connected(graph, nodes["belfast"], nodes["derry"]))


print("\n11th testing")


def is_twentieth_century(year):
    return year and 1901 <= year <= 2000


nodes, graph = load_graph("roadmap.dot", City.from_dict)
for node in nx.dfs_tree(graph, nodes["edinburgh"]):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
else:
    print("Not found")


print("\n12th testing")


def is_twentieth_century(city):
    return city.year and 1901 <= city.year <= 2000


nodes, graph = load_graph("roadmap.dot", City.from_dict)
city = dfs(graph, nodes["edinburgh"], is_twentieth_century)
print(city.name)
print("\n")
for city in depth_first_traverse(graph, nodes["edinburgh"]):
    print(city.name)


print("\n13th testing")
nodes, graph = load_graph("roadmap.dot", City.from_dict)
city1 = nodes["london"]
city2 = nodes["edinburgh"]


def distance(weights):
    return float(weights["distance"])


for city in dijkstra_shortest_path(graph, city1, city2, distance):
    print(city.name)

print("\nCompare to Networkx implementation:")


def weight(node1, node2, weights):
    return distance(weights)


for city in nx.dijkstra_path(graph, city1, city2, weight):
    print(city.name)
