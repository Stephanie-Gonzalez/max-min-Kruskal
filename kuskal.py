# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import random
import networkx as nx
import matplotlib.pyplot as plt

class UnionFind:
    """Estructura de datos Union-Find para búsqueda de conjuntos disjuntos"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_root, j_root = self.find(i), self.find(j)
        if i_root == j_root:
            return
        if self.rank[i_root] < self.rank[j_root]:
            i_root, j_root = j_root, i_root
        self.parent[j_root] = i_root
        if self.rank[i_root] == self.rank[j_root]:
            self.rank[i_root] += 1

def kruskal(edges, n):
    """Algoritmo de Kruskal para encontrar árboles de mínimo y máximo coste"""
    edges.sort()
    uf = UnionFind(n)
    min_tree, max_tree = [], []
    for weight, u, v in edges:
        if uf.find(u) == uf.find(v):
            continue
        uf.union(u, v)
        min_tree.append((u, v, weight))
        max_tree.append((u, v, -weight))
    return min_tree, max_tree

def generate_random_graph(n, p):
    """Genera un grafo aleatorio con pesos aleatorios"""
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                weight = random.randint(1, 100)
                edges.append((weight, i, j))
    return edges

# Ejemplo de uso:
if __name__ == '__main__':
    n = 5  # número de nodos
    p = 0.4  # probabilidad de que dos nodos estén conectados
    edges = generate_random_graph(n, p)
    print('Aristas generadas:', edges)
    min_tree, max_tree = kruskal(edges, n)
    print('Árbol de mínimo coste:', min_tree)
    print('Árbol de máximo coste:', max_tree)

    # Creamos el grafo original y los árboles de mínimo y máximo coste
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    min_tree_edges = [(u, v) for u, v, w in min_tree]
    max_tree_edges = [(u, v) for u, v, w in max_tree]

    # Creamos el layout del grafo
    pos = nx.spring_layout(G)

    # Dibujamos el grafo original
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.8)
    nx.draw_networkx_labels(G, pos, font_size=18, font_family='sans-serif')
    plt.title('Grafo original')
    plt.axis('off')
    plt