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
        print(f"{indentacion}Figura: {self.identificador}, Tipo: {self.tipo}, Área: {self.area}, Puntos: {self.puntos}")
        for hijo in self.hijos:
            hijo.imprimirArbol(nivel + 1)

    def agregarNodosAGrafo(self, grafo, nivel=0):
        etiqueta = f"{self.tipo}\n{self.area}\n{self.puntos}"
        grafo.add_node(self.identificador, etiqueta=etiqueta, subset=nivel)
        for hijo in self.hijos:
            hijo.agregarNodosAGrafo(grafo, nivel + 1)
            grafo.add_edge(self.identificador, hijo.identificador)

class ArbolFiguras:
    def __init__(self):
        
        self.raizConsola = NodoFigura("Figuras", " ", [], 0)
        self.tiposConsola = {
            "Triángulo Rectángulo": NodoFigura("Triángulos Rectángulos", " ", [], 0),
            "Cuadrado": NodoFigura("Cuadrados", " ", [], 0),
            "Rectángulo": NodoFigura("Rectángulos", " ", [], 0)
        }
        self.raizConsola.hijos.extend(self.tiposConsola.values())

        self.raiz = NodoFigura("Figuras", " ", " ", " ")
        self.tipos = {
            "Triángulo Rectángulo": NodoFigura("Triángulos Rectángulos", " ", " ", " "),
            "Cuadrado": NodoFigura("Cuadrados", " ", " ", " "),
            "Rectángulo": NodoFigura("Rectángulos", " ", " ", " ")
        }
        self.raiz.hijos.extend(self.tipos.values())
    
    
    def agregarFigura(self, figura):
        tipo = figura["tipo"]
        if tipo in self.tipos:
            numero = figura['identificador'].split('_')
            areaN = f"Area{numero[1]}"
            areaNodo = NodoFigura(f"{areaN} {figura['area']}", " ", " ", " ")
            areaNodoConsola = NodoFigura(f"{figura['identificador']}", figura['tipo'], figura['puntos'], figura['area'])
            for i, punto in enumerate(figura['puntos']):
                puntoName = f"R{numero[1]}"
                if 'Triángulo Rectángulo_' in figura['identificador']:
                    puntoName = f"T{numero[1]}"
                elif 'Cuadrado_' in figura['identificador']:
                    puntoName = f"C{numero[1]}"
                puntoNodo = NodoFigura(f"{puntoName}P{i+1} {[punto]}", " ", " ", " ")
                puntoNodoConsola = NodoFigura(f"{figura['identificador']}_P_{i+1}", "Punto", [punto], "")
                areaNodo.agregarHijo(puntoNodo)
                areaNodoConsola.agregarHijo(puntoNodoConsola)
            self.tipos[tipo].agregarHijo(areaNodo)
            self.tiposConsola[tipo].agregarHijo(areaNodoConsola)

    def imprimirArbol(self):
        self.raizConsola.imprimirArbol()

    def graficarArbol(self):
        grafo = nx.DiGraph()
        self.raiz.agregarNodosAGrafo(grafo)

        pos = self.jerarquia(grafo, self.raiz.identificador)
        plt.figure(figsize=(12, 8))

        nx.draw(grafo, pos, with_labels=True, node_size=4000, node_color="red", font_size=6, font_weight="bold", edge_color="gray")

        labels = nx.get_node_attributes(grafo, 'etiqueta')
        nx.draw_networkx_labels(grafo, pos, labels, font_size=8, verticalalignment='center', horizontalalignment='center')
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

arbolFiguras = ArbolFiguras()

def agregarFiguraAlArbol(figura):
    arbolFiguras.agregarFigura(figura)