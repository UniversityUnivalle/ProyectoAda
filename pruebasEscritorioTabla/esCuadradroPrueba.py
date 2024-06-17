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
    "P4",
    "LADO",
    "AREA"
]

resultadosArea = []
def areaCuadrado(puntos):
    os.system('cls')
    resultadosArea.append([puntos, "", "", "", "", "", ""])
    print(tabulate(resultadosArea, headersArea))
    input("Presione Enter Para Continuar...")

    os.system('cls')
    resultadosArea.append(["", puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1], "", ""])
    print(tabulate(resultadosArea, headersArea))
    input("Presione Enter Para Continuar...")
    
    lado = calcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1])
    os.system('cls')
    resultadosArea.append(["", "", "", "", "", lado, ""])
    print(tabulate(resultadosArea, headersArea))
    input("Presione Enter Para Continuar...")
    
    os.system('cls')
    resultadosArea.append(["", "", "", "", "", "", lado * lado])
    print(tabulate(resultadosArea, headersArea))
    input("Presione Enter Para Continuar...")
    
    return lado * lado

area = areaCuadrado([(1, 1), (1, 2), (2, 1), (2, 2)])
GenerarText(tabulate(resultadosArea, headersArea), [(1, 1), (1, 2), (2, 1), (2, 2)], "PruebaEscritorioAreaCuadradp", area)

headresEsCuadrado = [
    "PUNTOS",
    "len(puntos) != 4",
    "DISTANCIAS",
    "DISTANCIAS ORDENADAS",
    "D1",
    "D2",
    "D3",
    "D4",
    "D5",
    "D6",
    "RETORNO"
]

resultadosEsCuadrado = []
def esCuadrado(puntos):
    os.system("cls")
    resultadosEsCuadrado.append([puntos, "", "", "", "", "", "", "", "", "", ""])
    print(tabulate(resultadosEsCuadrado, headresEsCuadrado))
    input("Presione Enter Para Continuar...")

    os.system("cls")
    resultadosEsCuadrado.append(["", len(puntos) != 4, "", "", "", "", "", "", "", "", ""])
    print(tabulate(resultadosEsCuadrado, headresEsCuadrado))
    input("Presione Enter Para Continuar...")
    if len(puntos) != 4:
        os.system("cls")
        resultadosEsCuadrado.append(["", "", "", "", "", "", "", "", "", "", False])
        print(tabulate(resultadosEsCuadrado, headresEsCuadrado))
        input("Presione Enter Para Continuar...")
        return False

    distancias = calcularDistanciasRecursivo(puntos)

    os.system("cls")
    resultadosEsCuadrado.append(["", "", distancias, "", "", "", "", "", "", "", ""])
    print(tabulate(resultadosEsCuadrado, headresEsCuadrado))
    input("Presione Enter Para Continuar...")

    distancias = quickSortPersonalizado(distancias)

    os.system("cls")
    resultadosEsCuadrado.append(["", "", "", distancias, "", "", "", "", "", "", ""])
    print(tabulate(resultadosEsCuadrado, headresEsCuadrado))
    input("Presione Enter Para Continuar...")

    os.system("cls")
    resultadosEsCuadrado.append(["", "", "", "", distancias[0], distancias[1], distancias[2], distancias[3], distancias[4], distancias[5], ""])
    print(tabulate(resultadosEsCuadrado, headresEsCuadrado))
    input("Presione Enter Para Continuar...")

    os.system("cls")
    resultadosEsCuadrado.append(["", "", "", "", "", "", "", "", "", "", (distancias[0] == distancias[1] == distancias[2] == distancias[3] and distancias[4] == distancias[5])])
    print(tabulate(resultadosEsCuadrado, headresEsCuadrado))
    input("Presione Enter Para Continuar...")

    return (distancias[0] == distancias[1] == distancias[2] == distancias[3] and 
            distancias[4] == distancias[5])

esC = esCuadrado([(1, 1), (1, 2), (2, 1), (2, 2)])
GenerarText(tabulate(resultadosEsCuadrado, headresEsCuadrado), [(1, 1), (1, 2), (2, 1), (2, 2)], "PruebaEscritorioEsCuadrado", esC)