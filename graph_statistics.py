import networkx

file = "graph.gexf"

g = networkx.read_gexf(file)

print("Number of nodes: ", g.number_of_nodes())
print("Number of edges: ", g.number_of_edges())

print("Density: ", networkx.density(g))
#print("Average clustering: ", networkx.average_clustering(g))
#print("Average shortest path length: ", networkx.average_shortest_path_length(g))
#print("Diameter: ", networkx.diameter(g))

# nodes with highest degres (top 15)
print("Nodes with highest degree: ", sorted(g.degree, key=lambda x: x[1], reverse=True)[:15])

