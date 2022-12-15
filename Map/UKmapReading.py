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
