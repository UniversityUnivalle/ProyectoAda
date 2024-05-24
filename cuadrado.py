from distancia import calcularDistancia

# Función para calcular el área de un cuadrado
def areaCuadrado(puntos):
    lado = calcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1])
    return lado * lado

def esCuadrado(puntos):
    if len(puntos) != 4:
        return False

    distancias = [
        calcularDistancia(puntos[i][0], puntos[i][1], puntos[j][0], puntos[j][1])
        for i in range(4)
        for j in range(i + 1, 4)
    ]

    distancias.sort()
    return distancias[0] == distancias[1] == distancias[2] == distancias[3]

