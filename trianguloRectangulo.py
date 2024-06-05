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

def esTrianguloRectangulo(puntos):
    if len(puntos) != 3:
        return False

    distancias = calcularDistanciasRecursivo(puntos)
    distancias = elevarDistanciasCuadrado(distancias)

    distancias = quickSortPersonalizado(distancias)
    
    return distancias[0] + distancias[1] == distancias[2]
