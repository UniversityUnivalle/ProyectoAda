import matplotlib.pyplot as plt
import networkx as nx

class NodoFigura:
    def __init__(self, identificador, tipo, puntos, area):
        self.identificador = identificador
        self.tipo = tipo
        self.puntos = puntos
        self.area = area
        self.hijos = []

    def agregarHijo(self, nodoHijo):
        self.hijos.append(nodoHijo)

    def imprimirArbol(self, nivel=0):
        indentacion = "  " * nivel
        print(f"{indentacion}Figura: {self.identificador}, Tipo: {self.tipo}, Puntos: {self.puntos}, Área: {self.area}")
        for hijo in self.hijos:
            hijo.imprimirArbol(nivel + 1)

    def agregarNodosAGrafo(self, grafo, nivel=0):
        etiqueta = f"{self.tipo}\nPuntos: {self.puntos}"
        grafo.add_node(self.identificador, etiqueta=etiqueta, subset=nivel)
        for hijo in self.hijos:
            hijo.agregarNodosAGrafo(grafo, nivel + 1)
            grafo.add_edge(self.identificador, hijo.identificador)

class ArbolFiguras:
    def __init__(self):
        self.raiz = NodoFigura("Raiz", "Raiz", [], 0)
        self.tipos = {
            "Triángulo Rectángulo": NodoFigura("Triángulos Rectángulos", "Tipo", [], 0),
            "Cuadrado": NodoFigura("Cuadrados", "Tipo", [], 0),
            "Rectángulo": NodoFigura("Rectángulos", "Tipo", [], 0)
        }
        self.raiz.hijos.extend(self.tipos.values())

    def agregarFigura(self, figura):
        tipo = figura["tipo"]
        if tipo in self.tipos:
            nuevoNodo = NodoFigura(figura['identificador'], figura['tipo'], figura['puntos'], figura['area'])
            self.tipos[tipo].agregarHijo(nuevoNodo)

    def imprimirArbol(self):
        self.raiz.imprimirArbol()

    def graficarArbol(self):
        grafo = nx.DiGraph()
        self.raiz.agregarNodosAGrafo(grafo)

        pos = self.hierarchy_pos(grafo, self.raiz.identificador)
        plt.figure(figsize=(12, 8))

        nx.draw(grafo, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")

        labels = nx.get_node_attributes(grafo, 'tipo')
        labels = {k: f"{k}\n{v}" for k, v in labels.items()}

        nx.draw_networkx_labels(grafo, pos, labels, font_size=8)
        plt.title("Árbol de Figuras Geométricas")
        plt.show()

    def hierarchy_pos(self, G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
        pos = _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
        return pos

def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None, parsed=[]):
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
            pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap, vert_loc=vert_loc-vert_gap, xcenter=nextx, pos=pos, parent=root, parsed=parsed)
            
    return pos

# Crear el árbol de figuras
arbolFiguras = ArbolFiguras()

def agregarFiguraAlArbol(figura):
    arbolFiguras.agregarFigura(figura)
