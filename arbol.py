# Definir la estructura del nodo del árbol
class NodoFigura:
    def __init__(self, identificador, tipo, puntos, area):
        self.identificador = identificador
        self.tipo = tipo
        self.puntos = puntos
        self.area = area
        self.hijos = []

    def agregarHijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

    def imprimirArbol(self, nivel=0):
        indentacion = "  " * nivel
        print(f"{indentacion}Figura: {self.identificador}, Tipo: {self.tipo}, Puntos: {self.puntos}, Área: {self.area}")
        for hijo in self.hijos:
            hijo.imprimirArbol(nivel + 1)

# Crear la raíz del árbol
arbolFiguras = NodoFigura("Raiz", "Raiz", [], 0)

# Función para agregar figuras al árbol
def agregarFiguraAlArbol(figura, nodoPadre):
    nuevoNodo = NodoFigura(figura['identificador'], figura['tipo'], figura['puntos'], figura['area'])
    nodoPadre.agregarHijo(nuevoNodo)
    return nuevoNodo