print("**************** PROGRAMMED BY: *****************")
print("************** NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("**Python Stacks, Queues, and Priority Queues **")
print("*************** Dot Reading Files *******************")

import networkx as nx
from Graph import *

print(nx.nx_agraph.read_dot("roadmap.dot"))

Graph = nx.nx_agraph.read_dot("roadmap.dot")
print(Graph.nodes["london"])
