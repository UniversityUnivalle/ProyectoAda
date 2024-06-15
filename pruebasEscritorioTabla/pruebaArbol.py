# import matplotlib.pyplot as plt
# import networkx as nx

# grafo = nx.DiGraph()

# grafo.add_node("Figuras Lista n")
# grafo.add_node("Rectangulos")
# grafo.add_node("Triangulos")

# areasTraigulos = [8.0, 6.0, 10.0, 7.5, 28.217902119044922, 7.5]

# grafo.add_node(20.0)

# puntosRectangulos = [(1, 1), (5, 1), (1, -2), (5, -2)]


# puntos = [[(1, 1), (1, 5), (5, 1)], 
#           [(1, 1), (5, 1), (1, -2)], 
#           [(1, 1), (5, 1), (5, -2)],
#           [(1, 1), (1, -2), (5, -2)],
#           [(1, 5), (1, -2), (5, -2)],
#           [(5, 1), (1, -2), (5, -2)]]

# for i in puntosRectangulos:
#     grafo.add_node(i)

# for i in areasTraigulos:
#     grafo.add_node(i)

# for i in puntos:
#     for j in i:
#         grafo.add_node(j)

# grafo.add_edge("Figuras Lista n", "Rectangulos")
# grafo.add_edge("Figuras Lista n", "Triangulos")
# grafo.add_edge("Rectangulos", 20.0)

# for i in puntosRectangulos:
#     grafo.add_edge(20.0, i)

# for i in areasTraigulos:
#     grafo.add_edge("Triangulos", i)

# for  i in range(len(puntos)):
#     for j in range(i, len(areasTraigulos)):
#         for k in puntos[i]:
#             grafo.add_edge(areasTraigulos[j], k)
#         break

# pos = nx.spring_layout(grafo)

# nx.draw(grafo, pos, with_labels=True, node_color='skyblue', node_size=3000, edge_color='black', linewidths=1, font_size=12)

# plt.show()

import networkx as nx
import matplotlib.pyplot as plt

# Crea un grafo dirigido
G = nx.DiGraph()

# Agrega nodos y aristas al grafo
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")

G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("B", "D")
G.add_edge("C", "E")

# Dibuja el grafo
pos = nx.spring_layout(G)  # Posición de los nodos
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1, font_size=12)

# Muestra la gráfica
plt.show()