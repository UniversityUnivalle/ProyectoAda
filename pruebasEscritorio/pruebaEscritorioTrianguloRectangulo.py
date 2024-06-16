import sys
import os

# Agregar la ruta al proyecto
projectRoot = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(projectRoot)

from calcularDistanciaRecursivo import calcularDistanciasRecursivo, calcularDistancia
from mySort import quickSortPersonalizado

enter = "Presiona Enter para continuar..."


def areaTrianguloRectangulo(puntos):

    print("Calculando el área del triángulo rectángulo con puntos:", puntos)
    input(enter)
    xp1 = puntos[0][0] #(1, 2) -> xp1 = 1
    print(f"xp1 =>  {xp1} ")
    yp1 = puntos[0][1] #(1, 2) -> yp1 = 2
    print(f"xp1 =>  {yp1}")
    xp2 = puntos[1][0] #(4, 2) -> xp2 = 4
    print(f"xp1 => {xp2}" )
    yp2 = puntos[1][1] #(4, 2) -> yp2 = 2
    print(f"xp1 =>  {yp2}")
    xp3 = puntos[2][0] #(6, 3) -> xp3 = 6
    print(f"xp1 =>  {xp3}")
    yp3 = puntos[2][1] #(6, 3) -> yp3 = 3
    print(f"xp1 =>  {yp3}")

    area = 0.5 * abs((xp1 * (yp2 - yp3) ) + (xp2 * (yp3 - yp1)) + (xp3 * (yp1 - yp2)))
    print("Área del triángulo calculada:", area)
    input(enter)
    return area

def elevarDistanciasCuadrado(distancias, index=0):
    print("Elevando distancias al cuadrado:", distancias)
    input(enter)
    if index >= len(distancias):
        print("Distancias elevadas al cuadrado final:", distancias)
        input(enter)
        return distancias

    distancias[index] = distancias[index] ** 2
    print(f"Distancia en el índice {index} elevada al cuadrado:", distancias[index])
    input(enter)

    return elevarDistanciasCuadrado(distancias, index + 1)

def esTrianguloRectangulo(puntos):
    print("Verificando si los puntos forman un triángulo rectángulo:", puntos)
    input(enter)

    if len(puntos) != 3:
        print("No es un triángulo rectángulo: la cantidad de puntos no es 3")
        return False

    distancias = calcularDistanciasRecursivo(puntos)
    print("Distancias calculadas entre los puntos:", distancias)
    input(enter)

    distanciasCuadrado = elevarDistanciasCuadrado(distancias)
    print("Distancias elevadas al cuadrado:", distanciasCuadrado)
    input(enter)

    distanciasCuadrado = quickSortPersonalizado(distanciasCuadrado)
    print("Distancias ordenadas:", distanciasCuadrado)
    input(enter)

    # Verifica si se cumple el teorema de Pitágoras con una tolerancia pequeña para manejar errores de precisión
    esTrianguloRectangulo = abs(distanciasCuadrado[2] - (distanciasCuadrado[0] + distanciasCuadrado[1])) < 0.000000001
    print("¿Es triángulo rectángulo?", esTrianguloRectangulo)
    input(enter)

    return esTrianguloRectangulo

# Ejemplo de prueba
puntos = [(0, 0), (3, 0), (0, 4)]
print("Resultado de la verificación de triángulo rectángulo:", esTrianguloRectangulo(puntos))
print("Área del triángulo rectángulo:", areaTrianguloRectangulo(puntos))
