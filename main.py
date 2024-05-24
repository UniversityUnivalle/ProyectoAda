import matplotlib.pyplot as plt
import numpy as np
from verificarListas import verificarListas
from trianguloRectangulo import esTrianguloRectangulo,areaTrianguloRectangulo
from cuadrado import esCuadrado,areaCuadrado
from rectangulo import esRectangulo,areaRectangulo

# Función para graficar puntos y figuras en un plano cartesiano
def graficarPuntosYFiguras(puntos, titulo):
    x, y = zip(*puntos)  # Separar las coordenadas x e y
    plt.figure()  # Crear una nueva figura para graficar
    plt.scatter(x, y)  # Graficar los puntos en el plano

    # Anotar cada punto con sus coordenadas
    for i, punto in enumerate(puntos):
        plt.annotate(f"{punto}", (x[i], y[i]))

    # Si hay 4 puntos, verificar si forman un cuadrado o rectángulo
    if len(puntos) == 4:
        if esCuadrado(puntos) or esRectangulo(puntos):
            # Ordenar los puntos para dibujar la figura correctamente
            orden = sorted(puntos, key=lambda p: (p[0], p[1]))
            plt.plot(
                [orden[0][0], orden[1][0], orden[3][0], orden[2][0], orden[0][0]],
                [orden[0][1], orden[1][1], orden[3][1], orden[2][1], orden[0][1]],
                "r",
            )
            plt.title(titulo)
    # Si hay 3 puntos, verificar si forman un triángulo rectángulo
    elif len(puntos) == 3 and esTrianguloRectangulo(puntos):
        plt.plot(
            [p[0] for p in list(puntos) + [puntos[0]]],
            [p[1] for p in list(puntos) + [puntos[0]]],
            "g",
        )
        plt.title(titulo)

    # Mostrar la cuadrícula y la figura en la gráfica
    plt.grid(True)
    plt.show()


# # Función recursiva para generar combinaciones de puntos
# def generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio, combinaciones):
#     # Si la combinación actual tiene la longitud deseada, agregarla a la lista de combinaciones
#     if len(combinacionActual) == longitudDeseada:
#         combinaciones.append(combinacionActual[:]) #combinacionActual[:] -> Agrega una copia de la combinación actual 
#         return
#     # Iterar a partir del índice de inicio para generar combinaciones
#     for i in range(indiceInicio, len(puntos)):
#         combinacionActual.append(puntos[i]) # Agregar el punto actual a la combinación
#         generarCombinaciones(puntos, combinacionActual, longitudDeseada, i + 1, combinaciones) # Llamada recursiva
#         combinacionActual.pop() # Eliminar el último punto para probar otra combinación

def generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio, combinaciones):
    # Si la combinación actual tiene la longitud deseada, agregarla a la lista de combinaciones
    if len(combinacionActual) == longitudDeseada:
        combinaciones.append(combinacionActual[:])  # Agrega una copia de la combinación actual
        return

    # Condición de salida si el índice de inicio excede la longitud de los puntos
    if indiceInicio >= len(puntos):
        return

    # Incluir el punto actual en la combinación y llamar recursivamente
    combinacionActual.append(puntos[indiceInicio])
    generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio + 1, combinaciones)
    
    # Excluir el punto actual de la combinación y llamar recursivamente
    combinacionActual.pop()
    generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio + 1, combinaciones)


# Función para obtener todas las combinaciones de una longitud dada
def obtenerCombinaciones(puntos, longitudDeseada):
    combinaciones = []
    generarCombinaciones(puntos, [], longitudDeseada, 0, combinaciones)
    return combinaciones

arrayListas = [
    [(1, 1), (1, 5), (5, 1), (1, -2), (5, -2)],
    [(3, 20), (14, 9), (4, 5), (3, 2), (15, 2), (-4, 0), (7, -5)]
]

# Graficar todos los puntos del arrayListas
def graficarTodosLosPuntos(arrayListas):
    plt.figure()
    for lista in arrayListas:
        x, y = zip(*lista)
        plt.scatter(x, y)
        for i, punto in enumerate(lista):
            plt.annotate(f"{punto}", (x[i], y[i]))
    plt.title("Todos los puntos")
    plt.grid(True)
    plt.show()

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

# Verificar las listas
listasValidas = verificarListas(arrayListas)

# Arreglo para almacenar las figuras y sus áreas
figuras = []

# Arreglos para almacenar las figuras encontradas
triangulosRectangulos = []
cuadrados = []
rectangulos = []

# Para cada lista válida de puntos
for lista in listasValidas:
    combinaciones = []

    # Generar combinaciones de 3 y 4 puntos
    for r in range(3, 5):
        combinaciones += obtenerCombinaciones(lista, r)

    # Verificar cada combinación generada
    for comb in combinaciones:
        if len(comb) == 4:
            if esCuadrado(comb):
                area = areaCuadrado(comb)
                figura = {
                    "identificador": f"Cuadrado_{len(figuras)+1}",
                    "tipo": "Cuadrado",
                    "puntos": comb,
                    "area": area
                }
                cuadrados.append(figura)
                figuras.append(figura)
                agregarFiguraAlArbol(figura,arbolFiguras)
                print(f"Los puntos {comb} forman un cuadrado con área {area}.")
                graficarPuntosYFiguras(comb, "Cuadrado")
                agregarFiguraAlArbol(figura,arbolFiguras)
            elif esRectangulo(comb):
                area = areaRectangulo(comb)
                figura = {
                    "identificador": f"Rectángulo_{len(figuras)+1}",
                    "tipo": "Rectángulo",
                    "puntos": comb,
                    "area": area
                }
                rectangulos.append(figura)
                figuras.append(figura)
                agregarFiguraAlArbol(figura,arbolFiguras)
                print(f"Los puntos {comb} forman un rectángulo con área {area}.")
                graficarPuntosYFiguras(comb, "Rectángulo")
        elif len(comb) == 3 and esTrianguloRectangulo(comb):
            area = areaTrianguloRectangulo(comb)
            figura = {
                "identificador": f"TriánguloRectángulo_{len(figuras)+1}",
                "tipo": "Triángulo Rectángulo",
                "puntos": comb,
                "area": area
            }
            triangulosRectangulos.append(figura)
            figuras.append(figura)
            print(f"Los puntos {comb} forman un triángulo rectángulo con área {area}.")
            graficarPuntosYFiguras(comb, "Triángulo Rectángulo")
            agregarFiguraAlArbol(figura,arbolFiguras)
        else:
            print(f"Los puntos {comb} no forman una figura específica.")

# Imprimir las figuras encontradas y sus áreas
for figura in figuras:
    print(f"Figura: {figura['identificador']}, Tipo: {figura['tipo']}, Puntos: {figura['puntos']}, Área: {figura['area']}")

print("imprimiendo arbol")
# Imprimir el árbol de figuras
arbolFiguras.imprimirArbol()

# Grafica todos los puntos existentes del arrayListas
graficarTodosLosPuntos(arrayListas)

# Imprimir el conteo de figuras encontradas
print(f"Triángulos rectángulos encontrados: {len(triangulosRectangulos)}")
print(f"Cuadrados encontrados: {len(cuadrados)}")
print(f"Rectángulos encontrados: {len(rectangulos)}")
