from calcularDistanciaRecursivo import calcularDistanciasRecursivo,calcularDistancia
from mySort import quickSortPersonalizado

def areaTrianguloRectangulo(puntos):
    base = calcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1])
    altura = calcularDistancia(puntos[0][0], puntos[0][1], puntos[2][0], puntos[2][1])
    return 0.5 * base * altura

def elevarDistanciasCuadrado(distancias, index=0):
    if index >= len(distancias):
        return distancias
    distancias[index] = distancias[index] ** 2
    return elevarDistanciasCuadrado(distancias, index + 1)

# def esTrianguloRectangulo(puntos):
#     if len(puntos) != 3:
#         return False

#     distancias = calcularDistanciasRecursivo(puntos)
#     distancias = elevarDistanciasCuadrado(distancias)

#     distancias = quickSortPersonalizado(distancias)
    
#     return distancias[0] + distancias[1] == distancias[2]


def esTrianguloRectangulo(puntos):
    if len(puntos) != 3:
        return False
    
    distancias = calcularDistanciasRecursivo(puntos)
    distanciasCuadrado = elevarDistanciasCuadrado(distancias)
    distanciasCuadrado = quickSortPersonalizado(distanciasCuadrado)
    
    # Verifica si se cumple el teorema de Pitágoras con una tolerancia pequeña para manejar errores de precisión
    return abs(distanciasCuadrado[2] - (distanciasCuadrado[0] + distanciasCuadrado[1])) < 0.000000001 #1×10^-9 o -> 1e-9


 # a, b, c = distanciasCuadrado[0], distanciasCuadrado[1], distanciasCuadrado[2]

    # corregirErrorPrecision = 0.000000001
    
    # if abs(c - (a + b)) < corregirErrorPrecision:
    #     return True
    # else:
    #     return False