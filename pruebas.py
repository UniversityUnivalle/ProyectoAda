import matplotlib.pyplot as plt
from itertools import combinations

def distancia(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def es_cuadrado(puntos):
    if len(puntos) != 4:
        return False
    
    distancias = [distancia(puntos[i], puntos[j]) for i in range(4) for j in range(i + 1, 4)]
    distancias.sort()
    
    return distancias[0] == distancias[1] == distancias[2] == distancias[3]

def es_rectangulo(puntos):
    if len(puntos) != 4:
        return False
    
    distancias = [distancia(puntos[i], puntos[j]) for i in range(4) for j in range(i + 1, 4)]
    distancias.sort()
    
    return distancias[0] == distancias[1] and distancias[2] == distancias[3]

def es_triangulo_rectangulo(puntos):
    if len(puntos) != 3:
        return False
    
    distancias = [distancia(puntos[i], puntos[j]) ** 2 for i in range(3) for j in range(i + 1, 3)]
    distancias.sort()
    
    return distancias[0] + distancias[1] == distancias[2]

def graficar_puntos_y_figuras(puntos, titulo):
    x, y = zip(*puntos)
    plt.figure()
    plt.scatter(x, y)
    
    for i, punto in enumerate(puntos):
        plt.annotate(f'{punto}', (x[i], y[i]))
    
    if len(puntos) == 4:
        if es_cuadrado(puntos) or es_rectangulo(puntos):
            orden = sorted(puntos, key=lambda p: (p[0], p[1]))
            plt.plot([orden[0][0], orden[1][0], orden[3][0], orden[2][0], orden[0][0]], 
                     [orden[0][1], orden[1][1], orden[3][1], orden[2][1], orden[0][1]], 'r')
            plt.title(titulo)
    elif len(puntos) == 3 and es_triangulo_rectangulo(puntos):
        plt.plot([p[0] for p in list(puntos) + [puntos[0]]], [p[1] for p in list(puntos) + [puntos[0]]], 'g')
        plt.title(titulo)
    
    plt.grid(True)
    plt.show()

# Lista de puntos de ejemplo
listas_puntos = [
    [(1, 1), (1, 5), (5, 1), (1, -2), (5, -2)]
]

for puntos in listas_puntos:
    combinaciones = []
    for r in range(3, 5):
        combinaciones += list(combinations(puntos, r))
    
    for comb in combinaciones:
        if len(comb) == 4 and (es_cuadrado(comb) or es_rectangulo(comb)):
            print(f"Los puntos {comb} forman un cuadrado o un rectángulo.")
            graficar_puntos_y_figuras(comb, "Cuadrado o Rectángulo")
        elif len(comb) == 3 and es_triangulo_rectangulo(comb):
            print(f"Los puntos {comb} forman un triángulo rectángulo.")
            graficar_puntos_y_figuras(comb, "Triángulo Rectángulo")
        else:
            print(f"Los puntos {comb} no forman una figura específica.")
