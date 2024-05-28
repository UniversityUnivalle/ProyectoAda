class NodoFigura:
    def __init__(self, identificador, tipo, puntos, area):
        # Inicializa un nodo con identificador, tipo, puntos y área de la figura
        self.identificador = identificador
        self.tipo = tipo
        self.puntos = puntos
        self.area = area
        self.hijos = []  # Lista de hijos para representar una estructura de árbol

    def agregarHijo(self, nodoHijo):
        # Agrega un nodo hijo a la lista de hijos del nodo actual
        self.hijos.append(nodoHijo)

    def imprimirArbol(self, nivel=0):
        # Imprime el árbol desde el nodo actual, con una indentación que indica el nivel en el árbol.
        indentacion = "  " * nivel
        print(f"{indentacion}Figura: {self.identificador}, Tipo: {self.tipo}, Puntos: {self.puntos}, Área: {self.area}")
        for hijo in self.hijos:
            # Llama recursivamente a la función para imprimir los hijos
            hijo.imprimirArbol(nivel + 1)

class ArbolFiguras:
    def __init__(self):
        # Inicializa el árbol de figuras con una raíz y nodos de tipos predefinidos
        self.raiz = NodoFigura("Raiz", "Raiz", [], 0)
        self.tipos = {
            "Triángulo Rectángulo": NodoFigura("Triángulos Rectángulos", "Tipo", [], 0),
            "Cuadrado": NodoFigura("Cuadrados", "Tipo", [], 0),
            "Rectángulo": NodoFigura("Rectángulos", "Tipo", [], 0)
        }
        # Agrega los nodos de tipo como hijos de la raíz
        self.raiz.hijos.extend(self.tipos.values())

    def agregarFigura(self, figura):
        # Agrega una nueva figura al árbol bajo el tipo correspondiente
        tipo = figura["tipo"]
        if tipo in self.tipos:
            # Crea un nuevo nodo para la figura
            nuevoNodo = NodoFigura(figura['identificador'], figura['tipo'], figura['puntos'], figura['area'])
            # Agrega el nuevo nodo como hijo del nodo de tipo correspondiente.
            self.tipos[tipo].agregarHijo(nuevoNodo)

    def imprimirArbol(self):
        # Imprime todo el árbol desde la raíz
        self.raiz.imprimirArbol()

# Crear el árbol de figuras
arbolFiguras = ArbolFiguras()

# Función para agregar figuras al árbol
def agregarFiguraAlArbol(figura):
    # Utiliza el método agregarFigura del objeto arbolFiguras para agregar una nueva figura al árbol
    arbolFiguras.agregarFigura(figura)

