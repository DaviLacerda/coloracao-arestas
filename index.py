import networkx as nx
import matplotlib.pyplot as plt

# ler as arestas do arquivo txt
edges = []
with open('edges.txt', 'r') as f:
    for line in f:
        x, y = line.strip().split()
        edges.append((str(x), str(y)))

# criar o grafo
G = nx.Graph()
G.add_edges_from(edges)

# plotar o grafo
nx.draw(G, with_labels=True)
plt.show()
