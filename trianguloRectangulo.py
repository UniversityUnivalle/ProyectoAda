from distancia import calcularDistancia

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
