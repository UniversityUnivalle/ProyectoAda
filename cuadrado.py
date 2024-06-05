from calcularDistanciaRecursivo import calcularDistanciasRecursivo,calcularDistancia
from mySort import quickSortPersonalizado

def areaCuadrado(puntos):
    lado = calcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1])
    return lado * lado

def esCuadrado(puntos):
    if len(puntos) != 4:
        return False

    distancias = calcularDistanciasRecursivo(puntos)

    distancias = quickSortPersonalizado(distancias)

    return (distancias[0] == distancias[1] == distancias[2] == distancias[3] and 
            distancias[4] == distancias[5])