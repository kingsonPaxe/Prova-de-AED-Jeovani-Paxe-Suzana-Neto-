import networkx as nx
# Criação do grafo

class Grafos():
    def __init__(self):
        self.grafo = nx.Graph()

    # Função para adicionar arestas
    def adicionar_aresta(self, node1, node2):
        self.grafo.add_edge(node1, node2)
    
    # Função para atualizar e desenhar o grafo
    def get_structure(self):
        return nx.node_link_data(self.grafo)