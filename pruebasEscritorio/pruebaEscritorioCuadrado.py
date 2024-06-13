import sys
import os

# Agregar la ruta al proyecto
projectRoot = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(projectRoot)

from calcularDistanciaRecursivo import calcularDistanciasRecursivo, calcularDistancia
from mySort import quickSortPersonalizado

enter = "Presiona Enter para continuar..."


def areaCuadrado(puntos):
    print("Calculando el área del cuadrado con puntos:", puntos)
    input(enter)
    lado = calcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1])
    print("Lado del cuadrado calculado:", lado)
    input(enter)
    area = lado * lado
    print("Área del cuadrado calculada:", area)
    input(enter)
    return area

def esCuadrado(puntos):
    print("Verificando si los puntos forman un cuadrado:", puntos)
    input(enter)
    if len(puntos) != 4:
        print("No es un cuadrado: la cantidad de puntos no es 4")
        return False

    distancias = calcularDistanciasRecursivo(puntos)
    print("Distancias calculadas entre los puntos:", distancias)
    input(enter)

    distancias = quickSortPersonalizado(distancias)
    print("Distancias ordenadas:", distancias)
    input(enter)

    esCuadrado = (distancias[0] == distancias[1] == distancias[2] == distancias[3] and 
                   distancias[4] == distancias[5])
    print("¿Es cuadrado?", esCuadrado)
    input(enter)

    return esCuadrado

# Ejemplo de prueba
puntos = [(0, 0), (1, 0), (1, 1), (0, 1)]
print("Resultado de la verificación de cuadrado:", esCuadrado(puntos))
