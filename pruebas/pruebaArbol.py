import matplotlib.pyplot as plt
import networkx as nx

class NodoFigura:
    def __init__(self, identificador, etiqueta):
        self.identificador = identificador
        self.etiqueta = etiqueta
        self.hijos = []

    def agregarHijo(self, nodoHijo):
        self.hijos.append(nodoHijo)

    def imprimirArbol(self, nivel=0):
        indentacion = "  " * nivel
        print(f"{indentacion}{self.etiqueta}")
        for hijo in self.hijos:
            hijo.imprimirArbol(nivel + 1)

    def agregarNodosAGrafo(self, grafo, nivel=0):
        grafo.add_node(self.identificador, etiqueta=self.etiqueta, subset=nivel)
        for hijo in self.hijos:
            hijo.agregarNodosAGrafo(grafo, nivel + 1)
            grafo.add_edge(self.identificador, hijo.identificador)

class ArbolFiguras:
    def __init__(self, listasEvaluadas):
        self.raiz = NodoFigura("Figuras", f"Figuras\nListas Evaluadas:\n{listasEvaluadas}")
        self.tipos = {
            "Triángulos": NodoFigura("Triángulos", "Triángulos"),
            "Cuadrados": NodoFigura("Cuadrados", "Cuadrados"),
            "Rectángulos": NodoFigura("Rectángulos", "Rectángulos")
        }
        self.raiz.hijos.extend(self.tipos.values())

    def agregarFigura(self, figura):
        tipo = figura["tipo"]
        if tipo in self.tipos:
            nodoArea = NodoFigura(f"{figura['identificador']}_Área", f"Área: {figura['area']}")
            for i, punto in enumerate(figura['puntos']):
                nodoPunto = NodoFigura(f"{figura['identificador']}_Punto{i+1}", f"Punto {i+1}: {punto}")
                nodoArea.agregarHijo(nodoPunto)
            self.tipos[tipo].agregarHijo(nodoArea)

    def imprimirArbol(self):
        self.raiz.imprimirArbol()

    def graficarArbol(self):
        grafo = nx.DiGraph()
        self.raiz.agregarNodosAGrafo(grafo)

        pos = self.jerarquia(grafo, self.raiz.identificador)
        plt.figure(figsize=(12, 8))

        nx.draw(grafo, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")

        etiquetas = nx.get_node_attributes(grafo, 'etiqueta')
        etiquetas = {k: f"{v}" for k, v in etiquetas.items()}

        nx.draw_networkx_labels(grafo, pos, etiquetas, font_size=8)
        plt.title("Árbol de Figuras Geométricas")
        plt.show()

    def jerarquia(self, G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
        pos = _jerarquia(G, root, width, vert_gap, vert_loc, xcenter)
        return pos

def _jerarquia(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None, parsed=[]):
    if pos is None:
        pos = {root: (xcenter, vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)
        
    children = list(G.neighbors(root))
    if not isinstance(G, nx.DiGraph) and parent is not None:
        children.remove(parent)
        
    if len(children) != 0:
        dx = width / len(children)
        nextx = xcenter - width/2 - dx/2
        for child in children:
            nextx += dx
            pos = _jerarquia(G, child, width=dx, vert_gap=vert_gap, vert_loc=vert_loc-vert_gap, xcenter=nextx, pos=pos, parent=root, parsed=parsed)
            
    return pos

# Ejemplo de listas evaluadas
listasEvaluadas = [
    [(1, 1), (1, 2), (2, 1), (2, 2)],
    [(1, 1), (5, 1), (1, -2), (5, -2)]
]

# Crear el árbol de figuras
arbolFiguras = ArbolFiguras(listasEvaluadas)

# Ejemplo de figuras
figuras = [
    {"identificador": "Cuadrado1", "tipo": "Cuadrados", "puntos": [(1, 1), (1, 2), (2, 1), (2, 2)], "area": 1.0},
    {"identificador": "Rectángulo1", "tipo": "Rectángulos", "puntos": [(1, 1), (5, 1), (1, -2), (5, -2)], "area": 12}
]

for figura in figuras:
    arbolFiguras.agregarFigura(figura)

# Imprimir el árbol
arbolFiguras.imprimirArbol()

# Graficar el árbol
arbolFiguras.graficarArbol()
