from distancia import calcularDistancia

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
