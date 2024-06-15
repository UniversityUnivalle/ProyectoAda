from GenerarTxt import GenerarText
from tabulate import tabulate
import os

headers = [
    "PUNTOS",
    "I",
    "J",
    "DISTANCIAS",
    "distancias is None",
    "i >= len(puntos) - 1",
    "j >= len(puntos)",
    "X1",
    "Y1",
    "X2",
    "Y2",
    "FORMULA"
]

resultadosCalcularDistanciasRecursivo = []

def calcularDistancia(x1, y1, x2, y2):
    os.system('cls')
    resultadosCalcularDistanciasRecursivo.append(["", "", "", "", "", "", "", x1, y1, x2, y2, ""])
    print(tabulate(resultadosCalcularDistanciasRecursivo, headers))
    input("Presione Enter Para Continuar...")
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    os.system('cls')
    resultadosCalcularDistanciasRecursivo.append(["", "", "", "", "", "", "", "", "", "", "", distancia])
    print(tabulate(resultadosCalcularDistanciasRecursivo, headers))
    input("Presione Enter Para Continuar...")
    return distancia

def calcularDistanciasRecursivo(puntos, i=0, j=1, distancias=None):
    os.system('cls')
    resultadosCalcularDistanciasRecursivo.append([puntos, i, j, distancias, "", "", "", "", "", "", "", ""])
    print(tabulate(resultadosCalcularDistanciasRecursivo, headers))
    input("Presione Enter Para Continuar...")
    os.system('cls')
    resultadosCalcularDistanciasRecursivo.append(["", "", "", "", distancias is None, "", "", "", "", "", "", ""])
    print(tabulate(resultadosCalcularDistanciasRecursivo, headers))
    input("Presione Enter Para Continuar...")
    if distancias is None:
        distancias = []
    
    os.system('cls')
    resultadosCalcularDistanciasRecursivo.append(["", "", "", distancias, "", "", "", "", "", "", "", ""])
    print(tabulate(resultadosCalcularDistanciasRecursivo, headers))
    input("Presione Enter Para Continuar...")

    os.system('cls')
    resultadosCalcularDistanciasRecursivo.append(["", "", "", "", "", i >= len(puntos) - 1, "", "", "", "", "", ""])
    print(tabulate(resultadosCalcularDistanciasRecursivo, headers))
    input("Presione Enter Para Continuar...")

    if i >= len(puntos) - 1:
        os.system('cls')
        resultadosCalcularDistanciasRecursivo.append(["", "", "", distancias, "", "", "", "", "", "", "", ""])
        print(tabulate(resultadosCalcularDistanciasRecursivo, headers))
        input("Presione Enter Para Continuar...")
        return distancias

    os.system('cls')
    resultadosCalcularDistanciasRecursivo.append(["", "", "", "", "", "", j >= len(puntos), "", "", "", "", ""])
    print(tabulate(resultadosCalcularDistanciasRecursivo, headers))
    input("Presione Enter Para Continuar...")

    if j >= len(puntos):
        return calcularDistanciasRecursivo(puntos, i + 1, i + 2, distancias)

    distancias.append(calcularDistancia(puntos[i][0], puntos[i][1], puntos[j][0], puntos[j][1]))

    os.system('cls')
    resultadosCalcularDistanciasRecursivo.append(["", "", "", distancias, "", "", "", "", "", "", "", ""])
    print(tabulate(resultadosCalcularDistanciasRecursivo, headers))
    input("Presione Enter Para Continuar...")

    return calcularDistanciasRecursivo(puntos, i, j + 1, distancias)

calcularDistanciasRecursivo([(1, 1), (1, 4), (4, 1)])