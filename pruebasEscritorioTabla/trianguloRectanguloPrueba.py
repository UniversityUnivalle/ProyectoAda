from tabulate import tabulate
import os
import sys
# Agregar la ruta al proyecto
projectRoot = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(projectRoot)

from calcularDistanciaRecursivo import calcularDistanciasRecursivo
from mySort import quickSortPersonalizado
from GenerarTxt import GenerarText

headersAreaT = [
    "PUNTOS",
    "X PUNTO 1",
    "Y PUNTO 1",
    "X PUNTO 2",
    "Y PUNTO 2",
    "X PUNTO 3",
    "Y PUNTO 3",
    "AREA"
]

resultadosArea = []

def areaTrianguloRectangulo(puntos):

    os.system('cls')
    resultadosArea.append([puntos, puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1], puntos[2][0], puntos[2][1], ""])
    print(tabulate(resultadosArea, headersAreaT))
    input("Presione Enter Para Continuar...")

    xp1 = puntos[0][0] #(1, 2) -> xp1 = 1
    yp1 = puntos[0][1] #(1, 2) -> yp1 = 2
    xp2 = puntos[1][0] #(4, 2) -> xp2 = 4
    yp2 = puntos[1][1] #(4, 2) -> yp2 = 2
    xp3 = puntos[2][0] #(6, 3) -> xp3 = 6
    yp3 = puntos[2][1] #(6, 3) -> yp3 = 3

    area = 0.5 * abs((xp1 * (yp2 - yp3) ) + (xp2 * (yp3 - yp1)) + (xp3 * (yp1 - yp2)))

    os.system('cls')
    resultadosArea.append(["", "", "", "", "", "", "", area])
    print(tabulate(resultadosArea, headersAreaT))
    input("Presione Enter Para Continuar...")

    return area

area = areaTrianguloRectangulo([(7, -5), (-4, -5), (7, -24)])
GenerarText(tabulate(resultadosArea, headersAreaT), [(7, -5), (-4, -5), (7, -24)], "PruebaEscritorioAreaTrianguloRectangulo", area)

headresDistanciasCuadreado = [
    "DISTANCIAS", 
    "INDEX",
    "index >= len(distancias)",
    "DISTANCIA",
    "DISTANCIAS ELEVADA"
]

resultadosDistanciasCuadreado = []

def elevarDistanciasCuadrado(distancias, index=0):
    os.system("cls")
    dis = distancias[:]
    resultadosDistanciasCuadreado.append([dis, index, index >= len(distancias), "", ""])
    print(tabulate(resultadosDistanciasCuadreado, headresDistanciasCuadreado))
    input("Presiona Enter Para Continuar...")
    if index >= len(distancias):
        os.system("cls")
        resultadosDistanciasCuadreado.append([dis, "", "", "", ""])
        print(tabulate(resultadosDistanciasCuadreado, headresDistanciasCuadreado))
        input("Presiona Enter Para Continuar...")
        return distancias

    os.system("cls")
    distancia = distancias[index]
    resultadosDistanciasCuadreado.append(["", "", "", distancia, ""])
    print(tabulate(resultadosDistanciasCuadreado, headresDistanciasCuadreado))
    input("Presiona Enter Para Continuar...")

    distancias[index] = distancias[index] ** 2

    os.system("cls")
    resultadosDistanciasCuadreado.append(["", "", "", "", distancia ** 2])
    print(tabulate(resultadosDistanciasCuadreado, headresDistanciasCuadreado))
    input("Presiona Enter Para Continuar...")

    return elevarDistanciasCuadrado(distancias, index + 1)

headersEsTriangulo = [
    "PUNTOS",
    "len(puntos) != 3",
    "DISTANCIAS",
    "DISTANCIAS CUADRADO",
    "DISTANCIAS CUADRADO ORDENADAS",
    "RETORNO"
]

resultadosEsTriangulo = []

def esTrianguloRectangulo(puntos):

    os.system("cls")
    resultadosEsTriangulo.append([puntos, len(puntos) != 3, "", "", "", ""])
    print(tabulate(resultadosEsTriangulo, headersEsTriangulo))
    input("Presione Enter Para Continuar...")

    if len(puntos) != 3:
        os.system("cls")
        resultadosEsTriangulo.append(["", "", "", "", "", False])
        print(tabulate(resultadosEsTriangulo, headersEsTriangulo))
        input("Presione Enter Para Continuar...")
        return False
    
    distancias = calcularDistanciasRecursivo(puntos)

    os.system("cls")
    resultadosEsTriangulo.append(["", "", distancias, "", "", ""])
    print(tabulate(resultadosEsTriangulo, headersEsTriangulo))
    input("Presione Enter Para Continuar...")

    distanciasCuadrado = elevarDistanciasCuadrado(distancias)

    os.system("cls")
    resultadosEsTriangulo.append(["", "", "", distanciasCuadrado, "", ""])
    print(tabulate(resultadosEsTriangulo, headersEsTriangulo))
    input("Presione Enter Para Continuar...")

    distanciasCuadrado = quickSortPersonalizado(distanciasCuadrado)
    
    os.system("cls")
    resultadosEsTriangulo.append(["", "", "", "", distanciasCuadrado, ""])
    print(tabulate(resultadosEsTriangulo, headersEsTriangulo))
    input("Presione Enter Para Continuar...")

    os.system("cls")
    resultadosEsTriangulo.append(["", "", "", "", "", abs(distanciasCuadrado[2] - (distanciasCuadrado[0] + distanciasCuadrado[1])) < 0.000000001])
    print(tabulate(resultadosEsTriangulo, headersEsTriangulo))
    input("Presione Enter Para Continuar...")

    # Verifica si se cumple el teorema de Pitágoras con una tolerancia pequeña para manejar errores de precisión - diferencia absoluta(abs)
    return abs(distanciasCuadrado[2] - (distanciasCuadrado[0] + distanciasCuadrado[1])) < 0.000000001 #1×10^-9 o -> 1e-9

es = esTrianguloRectangulo([(7, -5), (-4, -5), (7, -24)])
GenerarText(tabulate(resultadosEsTriangulo, headersEsTriangulo), [(7, -5), (-4, -5), (7, -24)], "PruebaEscritorioEsTriangulo", es)
GenerarText(tabulate(resultadosDistanciasCuadreado, headresDistanciasCuadreado), "", "PruebaEscritorioDistanciasCuadreado", "")