from distancia import calcularDistancia

# Función para calcular el área de un triángulo rectángulo
def areaTrianguloRectangulo(puntos):
    base = calcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1])
    altura = calcularDistancia(puntos[0][0], puntos[0][1], puntos[2][0], puntos[2][1])
    return 0.5 * base * altura

def esTrianguloRectangulo(puntos):
    if len(puntos) != 3:
        return False

    distancias = [
        calcularDistancia(puntos[i][0], puntos[i][1], puntos[j][0], puntos[j][1]) ** 2
        for i in range(3)
        for j in range(i + 1, 3)
    ]

    distancias.sort()
    return distancias[0] + distancias[1] == distancias[2]
