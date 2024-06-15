from calcularDistanciaRecursivo import calcularDistanciasRecursivo,calcularDistancia
from mySort import quickSortPersonalizado

def areaRectangulo(puntos):
    lado1 = calcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1])
    lado2 = calcularDistancia(puntos[1][0], puntos[1][1], puntos[3][0], puntos[3][1])
    return lado1 * lado2

def esRectangulo(puntos):
    if len(puntos) != 4:
        return False

    distancias = calcularDistanciasRecursivo(puntos)

    distancias = quickSortPersonalizado(distancias)
    
    return (distancias[0] == distancias[1] and distancias[2] == distancias[3] and 
            distancias[4] == distancias[5])
