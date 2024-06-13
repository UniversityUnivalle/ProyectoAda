from tabulate import tabulate
import os

headersQuickSortPerzonalizado = [
    "ITERACIONES",
    "ARREGLO",
    "len(arreglo) <= 1",
    "PIVOTE",
    "IZQUIERDA",
    "MEDIO",
    "DERACHA",
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
        elseMesio =  not(((arreglo[index] < pivote) == True) or ((arreglo[index] > pivote) == True) == True)
        resultadosQuickSortPerzonalizado.append(["", "", "", "", "", "", "", "", "", arreglo[index] < pivote, arreglo[index] > pivote, elseMesio])
        print(tabulate(resultadosQuickSortPerzonalizado, headersQuickSortPerzonalizado))
        input("Presione Enter Para Continuar..")
        if arreglo[index] < pivote:
            izquierda.append(arreglo[index])
            os.system('cls')
            resultadosQuickSortPerzonalizado.append(["", "", "", "", izquierda, "", "", "", "", "", "", ""])
            print(tabulate(resultadosQuickSortPerzonalizado, headersQuickSortPerzonalizado))
            input("Presione Enter Para Continuar..")
        elif arreglo[index] > pivote:
            derecha.append(arreglo[index])
            os.system('cls')
            resultadosQuickSortPerzonalizado.append(["", "", "", "", "", "", derecha, "", "", "", "", ""])
            print(tabulate(resultadosQuickSortPerzonalizado, headersQuickSortPerzonalizado))
            input("Presione Enter Para Continuar..")
        else:
            medio.append(arreglo[index])
            os.system('cls')
            resultadosQuickSortPerzonalizado.append(["", "", "", "", "", medio, "", "", "", "", "", ""])
            print(tabulate(resultadosQuickSortPerzonalizado, headersQuickSortPerzonalizado))
            input("Presione Enter Para Continuar..")

        return particion(arreglo, pivote, izquierda, medio, derecha, index + 1)

    izquierda, medio, derecha = particion(arreglo, pivote, izquierda, medio, derecha)
    
    return quickSortPersonalizado(izquierda, i+1) + medio + quickSortPersonalizado(derecha, i+1)

def GenerarText(tabla, arreglo):
    with open("PruebaEscritorioQuickSortPerzonalizado.txt", "w") as file:
        file.write(f"Arreglo: {arreglo} \n")
        file.write(f"{tabla}\n")
        file.write(f"Resultado: {arreglo}")

arreglo = quickSortPersonalizado([3, 6, 8, 10, 1, 2, 1], 0)
GenerarText(tabulate(resultadosQuickSortPerzonalizado, headersQuickSortPerzonalizado), arreglo)
