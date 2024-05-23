import matplotlib.pyplot as plt
import numpy as np
from verificarListas import verificarListas
from itertools import combinations
from trianguloRectangulo import esTrianguloRectangulo
from cuadrado import esCuadrado
from rectangulo import esRectangulo

def graficarPuntosYFiguras(puntos, titulo):
    x, y = zip(*puntos)
    plt.figure()
    plt.scatter(x, y)
    
    for i, punto in enumerate(puntos):
        plt.annotate(f'{punto}', (x[i], y[i]))
    
    if len(puntos) == 4:
        if esCuadrado(puntos) or esRectangulo(puntos):
            orden = sorted(puntos, key=lambda p: (p[0], p[1]))
            plt.plot([orden[0][0], orden[1][0], orden[3][0], orden[2][0], orden[0][0]], 
                     [orden[0][1], orden[1][1], orden[3][1], orden[2][1], orden[0][1]], 'r')
            plt.title(titulo)
    elif len(puntos) == 3 and esTrianguloRectangulo(puntos):
        plt.plot([p[0] for p in list(puntos) + [puntos[0]]], [p[1] for p in list(puntos) + [puntos[0]]], 'g')
        plt.title(titulo)
    
    plt.grid(True)
    plt.show()

arrayListas = [
    [(1, 1), (1, 5), (5, 1), (1, -2), (5, -2), (6, 3)]
    
]




# Verificar las listas
listasValidas = verificarListas(arrayListas)


for lista in listasValidas:
    combinaciones = []
    for r in range(3, 5):
        combinaciones += list(combinations(lista, r))
    
    for comb in combinaciones:
        if len(comb) == 4 and (esCuadrado(comb) or esRectangulo(comb)):
            print(f"Los puntos {comb} forman un cuadrado o un rectángulo.")
            graficarPuntosYFiguras(comb, "Cuadrado o Rectángulo")
        elif len(comb) == 3 and esTrianguloRectangulo(comb):
            print(f"Los puntos {comb} forman un triángulo rectángulo.")
            graficarPuntosYFiguras(comb, "Triángulo Rectángulo")
        else:
            print(f"Los puntos {comb} no forman una figura específica.")