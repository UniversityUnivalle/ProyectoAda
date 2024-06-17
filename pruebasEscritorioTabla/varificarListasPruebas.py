from GenerarTxt import GenerarText
from tabulate import tabulate
import os

headersVerificarListas = [
    "LISTAS",
    "LISTAS VALIDAS",
    "I",
    "i >= len(arrayListas)",
    "LISTA",
    "len(lista) >= 3"
]

resultadosVerificarListas = []

def verificarListas(arrayListas, listasValidas, i=0):
    
    listValidas = listasValidas[:]
    os.system('cls')
    resultadosVerificarListas.append([arrayListas, listValidas, i, i >= len(arrayListas), "", ""])
    print(tabulate(resultadosVerificarListas, headersVerificarListas))
    input("Presione Enter Para Continuar...")

    if i >= len(arrayListas):
        os.system('cls')
        resultadosVerificarListas.append(["", listValidas, "", "", "", ""])
        print(tabulate(resultadosVerificarListas, headersVerificarListas))
        input("Presione Enter Para Continuar...")
        return listasValidas
    
    os.system('cls')
    resultadosVerificarListas.append(["", "", "", "", arrayListas[i], ""])
    print(tabulate(resultadosVerificarListas, headersVerificarListas))
    input("Presione Enter Para Continuar...")

    lista = arrayListas[i]

    os.system('cls')
    resultadosVerificarListas.append(["", "", "", "", "", len(lista) >= 3])
    print(tabulate(resultadosVerificarListas, headersVerificarListas))
    input("Presione Enter Para Continuar...")

    if len(lista) >= 3:
        listasValidas.append(lista)
        os.system('cls')
        listVali = listasValidas[:]
        resultadosVerificarListas.append(["", listVali, "", "", "", ""])
        print(tabulate(resultadosVerificarListas, headersVerificarListas))
        input("Presione Enter Para Continuar...")
    else:
        listasValidas.append(lista)
        os.system('cls')
        resultadosVerificarListas.append(["", "", "", "", lista, ""])
        print(tabulate(resultadosVerificarListas, headersVerificarListas))
        print(f"La lista {lista} no tiene suficientes puntos.")
        input("Presione Enter Para Continuar...")

    return verificarListas(arrayListas, listasValidas, i + 1)

arrayListas = [
    [(1, 1), (1, 5), (5, 1), (1, -2), (5, -2)],
    [(1, 1), (1, 2), (2, 1), (2, 2)],
    [(2, 1), (1, 2), (2, 3), (3, 2)],
    [(1, 2), (2, 4)],
    [(3, 20), (14, 9), (4, 5), (3, 2), (15, 2), (24, -5), (7, -5), (-4, -5), (7, -24)]
]

listasValidas = verificarListas(arrayListas, [])
GenerarText(tabulate(resultadosVerificarListas, headersVerificarListas), [
    [(1, 1), (1, 5), (5, 1), (1, -2), (5, -2)],
    [(1, 1), (1, 2), (2, 1), (2, 2)],
    [(2, 1), (1, 2), (2, 3), (3, 2)],
    [(1, 2), (2, 4)],
    [(3, 20), (14, 9), (4, 5), (3, 2), (15, 2), (24, -5), (7, -5), (-4, -5), (7, -24)]
], "PruebEscritorioVerificarListas", listasValidas)