from calcularDistanciaRecursivo import calcularDistanciasRecursivo,calcularDistancia
from mySort import quickSortPersonalizado

def areaTrianguloRectangulo(puntos):

    xp1 = puntos[0][0] #(1, 2) -> xp1 = 1
    yp1 = puntos[0][1] #(1, 2) -> yp1 = 2
    xp2 = puntos[1][0] #(4, 2) -> xp2 = 4
    yp2 = puntos[1][1] #(4, 2) -> yp2 = 2
    xp3 = puntos[2][0] #(6, 3) -> xp3 = 6
    yp3 = puntos[2][1] #(6, 3) -> yp3 = 3

    area = 0.5 * abs((xp1 * (yp2 - yp3) ) + (xp2 * (yp3 - yp1)) + (xp3 * (yp1 - yp2)))

    return area


def elevarDistanciasCuadrado(distancias, index=0):
    if index >= len(distancias):
        return distancias
    distancias[index] = distancias[index] ** 2
    return elevarDistanciasCuadrado(distancias, index + 1)

def esTrianguloRectangulo(puntos):
    if len(puntos) != 3:
        return False
    
    distancias = calcularDistanciasRecursivo(puntos)
    distanciasCuadrado = elevarDistanciasCuadrado(distancias)
    distanciasCuadrado = quickSortPersonalizado(distanciasCuadrado)
    
    # Verifica si se cumple el teorema de Pitágoras con una tolerancia pequeña para manejar errores de precisión
    return abs(distanciasCuadrado[2] - (distanciasCuadrado[0] + distanciasCuadrado[1])) < 0.000000001 #1×10^-9 o -> 1e-9



 #  a, b, c = distanciasCuadrado[0], distanciasCuadrado[1], distanciasCuadrado[2]

    # corregirErrorPrecision = 0.000000001
    
    # if abs(c - (a + b)) < corregirErrorPrecision:
    #     return True
    # else:
    #     return False