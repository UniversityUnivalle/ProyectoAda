import matplotlib.pyplot as plt
import numpy as np
from verificarListas import verificarListas
from trianguloRectangulo import esTrianguloRectangulo
from cuadrado import esCuadrado
from rectangulo import esRectangulo


#Función para graficar puntos y figuras en un plano cartesiano
def graficarPuntosYFiguras(puntos, titulo):
    x, y = zip(*puntos)#Separar las coordenadas x e y
    plt.figure() #Crear una nueva figura para graficar
    plt.scatter(x, y) #Graficar los puntos en el plano

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

# Función recursiva para generar combinaciones de puntos
def generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio, combinaciones):
    # Si la combinación actual tiene la longitud deseada, agregarla a la lista de combinaciones
    if len(combinacionActual) == longitudDeseada:
        combinaciones.append(combinacionActual[:]) #combinacionActual[:] -> Agrega una copia de la combinación actual 
        return
    # Iterar a partir del índice de inicio para generar combinaciones
    for i in range (indiceInicio, len(puntos)):
        combinacionActual.append(puntos[i])# Agregar el punto actual a la combinación
        generarCombinaciones(puntos, combinacionActual, longitudDeseada, i + 1, combinaciones)# Llamada recursiva
        combinacionActual.pop()# Eliminar el último punto para probar otra combinación

# Función para obtener todas las combinaciones de una longitud dada
def obetenerCombinaciones (puntos, longitudDeseada):
    combinaciones = [] 
    generarCombinaciones(puntos, [], longitudDeseada, 0, combinaciones)
    return combinaciones

arrayListas = [
    [(1, 1), (1, 5), (5, 1), (1, -2), (5, -2)]
]

# Verificar las listas
listasValidas = verificarListas(arrayListas)

# Para cada lista válida de puntos
for lista in listasValidas:
    combinaciones = []

    # Generar combinaciones de 3 y 4 puntos
    for r in range(3, 5):
        combinaciones += obetenerCombinaciones(lista, r)

    # Verificar cada combinación generada
    for comb in combinaciones:
        if len(comb) == 4 and (esCuadrado(comb) or esRectangulo(comb)):
            print(f"Los puntos {comb} forman un cuadrado o un rectángulo.")
            graficarPuntosYFiguras(comb, "Cuadrado o Rectángulo")
        elif len(comb) == 3 and esTrianguloRectangulo(comb):
            print(f"Los puntos {comb} forman un triángulo rectángulo.")
            graficarPuntosYFiguras(comb, "Triángulo Rectángulo")
        else:
            print(f"Los puntos {comb} no forman una figura específica.")


# def CrearCombinacion(i, j, k, lista):
#     if k < len(lista):
#         print(lista[i], lista[j], lista[k])
#         CrearCombinacion(i, j, k + 1, lista)


# def addSegundoPunto(i, j, lista):
#     if j < len(lista):
#         CrearCombinacion(i, j, j + 1, lista)
#         addSegundoPunto(i, j + 1, lista)


# def firsCombination(i, lista):
#     if i < len(lista):
#         addSegundoPunto(0, i + 1, lista[i])
#         firsCombination(i + 1, lista)

# firsCombination(0, listasValidas)