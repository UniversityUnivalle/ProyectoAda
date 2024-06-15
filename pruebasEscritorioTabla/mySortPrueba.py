from GenerarTxt import GenerarText
from tabulate import tabulate
import os

headersQuickSortPerzonalizado = [
    "ITERACIONES",
    "ARREGLO",
    "len(arreglo) <= 1",
    "PIVOTE",
    "IZQUIERDA",
    "MEDIO",
    "DERECHA",
    "INDEX",
    "index == len(arreglo)",
    "arreglo[index] < pivote",
    "arreglo[index] > pivote",
    "else"
]

resultadosQuickSortPerzonalizado = []

def quickSortPersonalizado(arreglo, i):
    os.system('cls')
    resultadosQuickSortPerzonalizado.append([i, arreglo, len(arreglo) <= 1, "", "", "", "", "", "", "", "", ""])
    print(tabulate(resultadosQuickSortPerzonalizado, headersQuickSortPerzonalizado))
    input("Presione Enter Para Continuar..")
    if len(arreglo) <= 1:
        os.system('cls')
        resultadosQuickSortPerzonalizado.append(["", arreglo, "", "" "", "", "", "", "", "", "", ""])
        print(tabulate(resultadosQuickSortPerzonalizado, headersQuickSortPerzonalizado))
        input("Presione Enter Para Continuar..")
        return arreglo

    pivote = arreglo[0]
    izquierda = []
    medio = []
    derecha = []

    os.system('cls')
    resultadosQuickSortPerzonalizado.append(["", "", "", pivote, [], [], [], "", "", "", "", ""])
    print(tabulate(resultadosQuickSortPerzonalizado, headersQuickSortPerzonalizado))
    input("Presione Enter Para Continuar..")
    def particion(arreglo, pivote, izquierda, medio, derecha, index=0):
        os.system('cls')
        resultadosQuickSortPerzonalizado.append(["", "", "", "", "", "", "", index, index == len(arreglo), "", "", ""])
        print(tabulate(resultadosQuickSortPerzonalizado, headersQuickSortPerzonalizado))
        input("Presione Enter Para Continuar..")
        if index == len(arreglo):
            os.system('cls')
            resultadosQuickSortPerzonalizado.append(["", "", "", "", izquierda, medio, derecha, "", "", "", "", ""])
            print(tabulate(resultadosQuickSortPerzonalizado, headersQuickSortPerzonalizado))
            input("Presione Enter Para Continuar..")
            return izquierda, medio, derecha
        os.system('cls')
        elseMedio =  not(((arreglo[index] < pivote) == True) or ((arreglo[index] > pivote) == True) == True)
        resultadosQuickSortPerzonalizado.append(["", "", "", "", "", "", "", "", "", arreglo[index] < pivote, arreglo[index] > pivote, elseMedio])
        print(tabulate(resultadosQuickSortPerzonalizado, headersQuickSortPerzonalizado))
        input("Presione Enter Para Continuar..")
        if arreglo[index] < pivote:
            izquierda.append(arreglo[index])
            os.system('cls')
            izz = izquierda[:]
            resultadosQuickSortPerzonalizado.append(["", "", "", "", izz, "", "", "", "", "", "", ""])
            print(tabulate(resultadosQuickSortPerzonalizado, headersQuickSortPerzonalizado))
            input("Presione Enter Para Continuar..")
        elif arreglo[index] > pivote:
            derecha.append(arreglo[index])
            os.system('cls')
            dee = derecha[:]
            resultadosQuickSortPerzonalizado.append(["", "", "", "", "", "", dee, "", "", "", "", ""])
            print(tabulate(resultadosQuickSortPerzonalizado, headersQuickSortPerzonalizado))
            input("Presione Enter Para Continuar..")
        else:
            medio.append(arreglo[index])
            os.system('cls')
            mee = medio[:]
            resultadosQuickSortPerzonalizado.append(["", "", "", "", "", mee, "", "", "", "", "", ""])
            print(tabulate(resultadosQuickSortPerzonalizado, headersQuickSortPerzonalizado))
            input("Presione Enter Para Continuar..")

        return particion(arreglo, pivote, izquierda, medio, derecha, index + 1)

    izquierda, medio, derecha = particion(arreglo, pivote, izquierda, medio, derecha)
    
    return quickSortPersonalizado(izquierda, i+1) + medio + quickSortPersonalizado(derecha, i+1)

arreglo = quickSortPersonalizado([3, 6, 8, 10, 1, 2, 1], 0)
GenerarText(tabulate(resultadosQuickSortPerzonalizado, headersQuickSortPerzonalizado), arreglo, "PruebaEscritorioQuickSortPerzonalizado", arreglo)