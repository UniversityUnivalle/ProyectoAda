import sys
import os

# Agregar la ruta al proyecto
projectRoot = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(projectRoot)

from calcularDistanciaRecursivo import calcularDistanciasRecursivo, calcularDistancia
from mySort import quickSortPersonalizado

def areaRectangulo(puntos):
    print("Calculando el área del rectángulo con puntos:", puntos)
    input("Enter...")

    lado1 = calcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1])
    print("Lado 1 del rectángulo calculado:", lado1)
    input("Enter...")

    lado2 = calcularDistancia(puntos[1][0], puntos[1][1], puntos[2][0], puntos[2][1])
    print("Lado 2 del rectángulo calculado:", lado2)
    input("Enter...")

    area = lado1 * lado2
    print("Área del rectángulo calculada:", area)
    input("Enter...")

    return area

def esRectangulo(puntos):
    print("Verificando si los puntos forman un rectángulo:", puntos)
    input("Enter...")

    if len(puntos) != 4:
        print("No es un rectángulo: la cantidad de puntos no es 4")
        return False

    distancias = calcularDistanciasRecursivo(puntos)
    print("Distancias calculadas entre los puntos:", distancias)
    input("Enter...")

    distancias = quickSortPersonalizado(distancias)
    print("Distancias ordenadas:", distancias)
    input("Enter...")

    es_rectangulo = (distancias[0] == distancias[1] and distancias[2] == distancias[3] and 
                     distancias[4] == distancias[5])
    print("¿Es rectángulo?", es_rectangulo)
    input("Enter...")

    return es_rectangulo

# Ejemplo de prueba
puntos = [(0, 0), (2, 0), (2, 1), (0, 1)]
print("Resultado de la verificación de rectángulo:", esRectangulo(puntos))
print("Área del rectángulo:", areaRectangulo(puntos))
