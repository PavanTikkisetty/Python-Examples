import networkx as nx
import matplotlib.pyplot as plt
G = nx.read_edgelist('C:/Users/pavan/Desktop/datasets/facebook_combined.txt')
nx.draw(G)
plt.show(G)
