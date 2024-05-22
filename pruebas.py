# Libreria para graficar
import matplotlib.pyplot as plt
import numpy as np

# arreglos de prueba
ejemplo_1 = [[0, 0], [0, 2], [2, 0], [2, 2]]
ejemplo_2 = [[1, 1], [1, 4], [4, 1], [4, 4]]
ejemplo_3 = [[0, 0], [2, 0], [1, 1], [1, -1]]
ejemplo_4 = [[2, 3], [5, 6], [2, 6], [5, 3]]
ejemplo_5 = [[10, 10], [10, 14], [14, 10], [14, 14]]
ejemplo_6 = [[0, 0], [3, 3], [6, 0], [3, -3]]
ejemplo_7 = [[5, 5], [5, 8], [8, 5], [8, 8]]
ejemplo_8 = [[1, 2], [1, 5], [4, 2], [4, 5]]
ejemplo_9 = [[7, 8], [7, 11], [10, 8], [10, 11]]
ejemplo_10 = [[3, 3], [3, 7], [7, 3], [7, 7]]


#Funcion para graficar, se puede mejorar o cambiar
def graficarPuntos(lista):
    # Extraer coordenadas X e Y de la lista
    coordenadas_x = [punto[0] for punto in lista]
    coordenadas_y = [punto[1] for punto in lista]
    fig, ax = plt.subplots()
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_title("Puntos en el plano cartesiano")
    ax.grid()
    ax.set_ylim(-1 * np.max(coordenadas_y), np.max(coordenadas_y) + 1)
    ax.set_xlim(-1 * np.max(coordenadas_x), np.max(coordenadas_x) + 1)
    ax.axvline(color="black")
    ax.axhline(color="black")

    # Unir los puntos con una línea cerrada
    for i in range(len(coordenadas_x)):
        x1 = coordenadas_x[i]
        y1 = coordenadas_y[i]
        x2 = coordenadas_x[(i + 1) % len(coordenadas_x)]
        y2 = coordenadas_y[(i + 1) % len(coordenadas_y)]
        ax.plot([x1, x2], [y1, y2], marker="o", color="blue", linewidth=2)

    # Graficar los puntos individuales y mostrar sus coordenadas
    for i, punto in enumerate(lista):
        x, y = punto
        ax.scatter(x, y, marker="o", color="blue", s=50)
        ax.annotate(f"({x},{y})", (x, y + 0.1), ha="center", va="bottom", fontsize=8)

    plt.show()


# graficarPuntos(ejemplo_1)


#Formula para calcular distancias entre puntos
def calcularDistancia(x1: int, x2: int, y1: int, y2: int):
    return ((x2 - x1) ** 2 + (y1 - y2) ** 2) ** 0.5


# Funcion para realizar las distancias entre todos los puntos de una lista
def calcularDistanciasLista(j: int, i: int, lista: list):
    if j < len(lista):
        if j != i:
            print(
                lista[i],
                lista[j],
                calcularDistancia(lista[i][0], lista[j][0], lista[i][1], lista[j][1]),
            )
            calcularDistanciasLista(j + 1, i, lista)
        else:
            calcularDistanciasLista(j + 1, i, lista)

# Funcion para recorrer una lista y pasarla a la funcion calculardistaciasLista y las compare con el resto de la lista
def recorrerLista(i, lista):
    if i < len(lista):
        calcularDistanciasLista(0, i, lista)
        recorrerLista(i + 1, lista)

recorrerLista(0, ejemplo_3)