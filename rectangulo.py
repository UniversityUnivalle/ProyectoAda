from distancia import calcularDistancia

# Función para calcular el área de un rectángulo
def areaRectangulo(puntos):
    lado1 = calcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1])
    lado2 = calcularDistancia(puntos[1][0], puntos[1][1], puntos[2][0], puntos[2][1])
    return lado1 * lado2

def esRectangulo(puntos):
    if len(puntos) != 4:
        return False

    distancias = [
        calcularDistancia(puntos[i][0], puntos[i][1], puntos[j][0], puntos[j][1])
        for i in range(4)
        for j in range(i + 1, 4)
    ]

    distancias.sort()
    return distancias[0] == distancias[1] and distancias[2] == distancias[3]
