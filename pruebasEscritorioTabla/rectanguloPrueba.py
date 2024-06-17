from tabulate import tabulate
import os
import sys
# Agregar la ruta al proyecto
projectRoot = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(projectRoot)

from calcularDistanciaRecursivo import calcularDistanciasRecursivo,calcularDistancia
from mySort import quickSortPersonalizado
from GenerarTxt import GenerarText

headersArea = [
    "PUNTOS",
    "P1",
    "P2",
    "P3",
    "LADO1",
    "LADO2",
    "AREA"
]

resultadosArea = []

def areaRectangulo(puntos):
    os.system("cls")
    resultadosArea.append([puntos, puntos[0], puntos[1], puntos[3], "", "", ""])
    print(tabulate(resultadosArea, headersArea))
    input("Presione Enter Para Continuar...")

    lado1 = calcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1])

    os.system("cls")
    resultadosArea.append(["", "", "", "", lado1, "", ""])
    print(tabulate(resultadosArea, headersArea))
    input("Presione Enter Para Continuar...")

    lado2 = calcularDistancia(puntos[1][0], puntos[1][1], puntos[3][0], puntos[3][1])

    os.system("cls")
    resultadosArea.append(["", "", "", "", "", lado2, ""])
    print(tabulate(resultadosArea, headersArea))
    input("Presione Enter Para Continuar...")

    os.system("cls")
    resultadosArea.append(["", "", "", "", "", "", lado1 * lado2])
    print(tabulate(resultadosArea, headersArea))
    input("Presione Enter Para Continuar...")

    return lado1 * lado2

area = areaRectangulo([(1, 1), (5, 1), (1, -2), (5, -2)])
GenerarText(tabulate(resultadosArea, headersArea), [(1, 1), (5, 1), (1, -2), (5, -2)], "PruebaEscritorioAreaRectangulo", area)

headersEsRectangulo = [
    "PUNTOS",
    "len(puntos) != 4",
    "DISTANCIAS",
    "DISTANCIAS ORDENADAS",
    "RETORNO"
]

resultadosEsRectangulo = []

def esRectangulo(puntos):
    os.system("cls")
    resultadosEsRectangulo.append([puntos, len(puntos) != 4, "", "", ""])
    print(tabulate(resultadosEsRectangulo, headersEsRectangulo))
    input("Presione Enter Para Continuar..")
    if len(puntos) != 4:
        os.system("cls")
        resultadosEsRectangulo.append(["", "", "", "", False])
        print(tabulate(resultadosEsRectangulo, headersEsRectangulo))
        input("Presione Enter Para Continuar..")
        return False

    distancias = calcularDistanciasRecursivo(puntos)

    os.system("cls")
    resultadosEsRectangulo.append(["", "", distancias, "", ""])
    print(tabulate(resultadosEsRectangulo, headersEsRectangulo))
    input("Presione Enter Para Continuar..")

    distancias = quickSortPersonalizado(distancias)
    os.system("cls")
    resultadosEsRectangulo.append(["", "", "", distancias, ""])
    print(tabulate(resultadosEsRectangulo, headersEsRectangulo))
    input("Presione Enter Para Continuar..")

    os.system("cls")
    resultadosEsRectangulo.append(["", "", "", "", (distancias[0] == distancias[1] and distancias[2] == distancias[3] and distancias[4] == distancias[5])])
    print(tabulate(resultadosEsRectangulo, headersEsRectangulo))
    input("Presione Enter Para Continuar..")
    
    return (distancias[0] == distancias[1] and distancias[2] == distancias[3] and 
            distancias[4] == distancias[5])

es = esRectangulo([(1, 1), (5, 1), (1, -2), (5, -2)])
GenerarText(tabulate(resultadosEsRectangulo, headersEsRectangulo), [(1, 1), (5, 1), (1, -2), (5, -2)], "PruebaEscritorioEsRectangulo", es)