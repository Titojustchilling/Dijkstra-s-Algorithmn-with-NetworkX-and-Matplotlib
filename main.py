import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
nodeList = [1, 2, 3, 4, 5, 6, 7, 8]
edges = [ 
    (1, 2, {"weight": 8}), 
    (1, 3, {"weight": 3}), 
    (1, 4, {"weight": 5}), 
    (2, 3, {"weight": 2}), 
    (2, 4, {"weight": 1}),
    (2, 5, {"weight": 8}),
    (3, 5, {"weight": 4}), 
    (3, 6, {"weight": 7}), 
    (3, 7, {"weight": 8}), 
    (4, 5, {"weight": 6}), 
    (4, 6, {"weight": 4}), 
    (4, 7, {"weight": 2}), 
    (5, 6, {"weight": 3}), 
    (5, 7, {"weight": 4}), 
    (6, 7, {"weight": 5}),
    (6, 8, {"weight": 6}),
    (7, 8, {"weight": 2})
]

G.add_nodes_from(nodeList)
G.add_edges_from(edges)
origin = input("What node will be the origin? ") 
selection = input("What node are you selecting? ") 

weight = nx.shortest_path_length(G, int(origin), int(selection), weight="weight")

shortest = nx.shortest_path(G, int(origin), int(selection), method='dijkstra')

pos = nx.circular_layout(G)  
labels = nx.get_edge_attributes(G, 'weight')  

nx.draw(G, pos, with_labels=True, node_color='red', node_size=800)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

#path_edges = list(zip(shortest, shortest[1:]))
path_edges = shortest[1:]
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='black', width=2)

plt.show()
print("the shortest path from node " + origin + " to " + selection + " is " + str(shortest) + " with the cost being " + str(weight)) 