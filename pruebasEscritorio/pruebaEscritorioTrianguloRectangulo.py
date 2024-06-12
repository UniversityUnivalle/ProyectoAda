import sys
import os

# Agregar la ruta al proyecto
projectRoot = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(projectRoot)

from calcularDistanciaRecursivo import calcularDistanciasRecursivo, calcularDistancia
from mySort import quickSortPersonalizado

def areaTrianguloRectangulo(puntos):
    print("Calculando el área del triángulo rectángulo con puntos:", puntos)
    input("Enter...")

    base = calcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1])
    print("Base del triángulo calculada:", base)
    input("Enter...")

    altura = calcularDistancia(puntos[0][0], puntos[0][1], puntos[2][0], puntos[2][1])
    print("Altura del triángulo calculada:", altura)
    input("Enter...")

    area = 0.5 * base * altura
    print("Área del triángulo calculada:", area)
    input("Enter...")

    return area

def elevarDistanciasCuadrado(distancias, index=0):
    print("Elevando distancias al cuadrado:", distancias)
    input("Enter...")
    if index >= len(distancias):
        print("Distancias elevadas al cuadrado final:", distancias)
        input("Enter...")
        return distancias

    distancias[index] = distancias[index] ** 2
    print(f"Distancia en el índice {index} elevada al cuadrado:", distancias[index])
    input("Enter...")

    return elevarDistanciasCuadrado(distancias, index + 1)

def esTrianguloRectangulo(puntos):
    print("Verificando si los puntos forman un triángulo rectángulo:", puntos)
    input("Enter...")

    if len(puntos) != 3:
        print("No es un triángulo rectángulo: la cantidad de puntos no es 3")
        return False

    distancias = calcularDistanciasRecursivo(puntos)
    print("Distancias calculadas entre los puntos:", distancias)
    input("Enter...")

    distanciasCuadrado = elevarDistanciasCuadrado(distancias)
    print("Distancias elevadas al cuadrado:", distanciasCuadrado)
    input("Enter...")

    distanciasCuadrado = quickSortPersonalizado(distanciasCuadrado)
    print("Distancias ordenadas:", distanciasCuadrado)
    input("Enter...")

    # Verifica si se cumple el teorema de Pitágoras con una tolerancia pequeña para manejar errores de precisión
    esTrianguloRectangulo = abs(distanciasCuadrado[2] - (distanciasCuadrado[0] + distanciasCuadrado[1])) < 0.000000001
    print("¿Es triángulo rectángulo?", esTrianguloRectangulo)
    input("Enter...")

    return esTrianguloRectangulo

# Ejemplo de prueba
puntos = [(0, 0), (3, 0), (0, 4)]
print("Resultado de la verificación de triángulo rectángulo:", esTrianguloRectangulo(puntos))
print("Área del triángulo rectángulo:", areaTrianguloRectangulo(puntos))
