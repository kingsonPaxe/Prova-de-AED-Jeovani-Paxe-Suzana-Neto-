import networkx as nx
import matplotlib.pyplot as plt

# Gerando um grafo aleatório com 10 vértices e probabilidade de aresta entre vértices de 0.3
G = nx.erdos_renyi_graph(10, 0.3)

# Visualizando o grafo gerado
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_size=12, font_weight='bold')
plt.title('Exemplo de Grafo Aleatório')
plt.show()

# Exibindo informações sobre o grafo
print("Número de vértices:", G.number_of_nodes())
print("Número de arestas:", G.number_of_edges())
print("Lista de arestas:", list(G.edges()))
