from GenerarTxt import GenerarText
from tabulate import tabulate
import os

headersGenerarCombinaciones = [
    "ITERACIONES",
    "PUNTOS",
    "COMBINACION ACTUAL",
    "LONGITUD",
    "INDICE INICIO",
    "COMBINACIONES",
    "len(combinacionActual) == longitudDeseada",
    "indiceInicio >= len(puntos)",
    "PUNTO",
    "Eliminar Ultimo"
]

headersEliminarUltimo = [
    "ITERACIONES",
    "LISTA",
    "NUEVA lISTA",
    "i == len(lista) - 1",
    "LISTA[i]"
]

headersObtenerCombinaciones = [
    "ITERACIONES",
    "PUNTOS",
    "LONGITUD",
    "COMBINACIONES"
]

resultadoGenerarCombinaciones = []
resultadosElimnarUltimo = []
resultadoObtenerCombinaciones = []

def eliminarUltimoLista(lista, i, nuevaLista):
    os.system('cls')
    lisini = lista[:]
    lisNew = nuevaLista[:]
    resultadosElimnarUltimo.append([i, lisini, lisNew, "", ""])
    print(tabulate(resultadosElimnarUltimo, headersEliminarUltimo))
    input("Presione Enter Para Continuar..")
    
    os.system('cls')
    resultadosElimnarUltimo.append(["", "", "", i == len(lista) - 1, ""])
    print(tabulate(resultadosElimnarUltimo, headersEliminarUltimo))
    input("Presione Enter Para Continuar..")
    if i == len(lista) - 1:
        lista[:] = nuevaLista
        os.system('cls')
        lisEli = lista[:]
        resultadosElimnarUltimo.append(["", lisEli, "", "", ""])
        print(tabulate(resultadosElimnarUltimo, headersEliminarUltimo))
        input("Presione Enter Para Continuar..")
        return

    os.system('cls')
    resultadosElimnarUltimo.append(["", "", "", "", lista[i]])
    print(tabulate(resultadosElimnarUltimo, headersEliminarUltimo))
    input("Presione Enter Para Continuar..")
    nuevaLista.append(lista[i])

    eliminarUltimoLista(lista, i + 1, nuevaLista)


def generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio, combinaciones, i = 0):
    os.system('cls')
    comini = combinacionActual[:]
    combinacionesCopi = combinaciones[:]
    resultadoGenerarCombinaciones.append([i, puntos, comini, longitudDeseada, indiceInicio, combinacionesCopi, len(combinacionActual) == longitudDeseada, "", "", ""])
    print(tabulate(resultadoGenerarCombinaciones, headersGenerarCombinaciones))
    input("Presione Enter Para Continuar..")
    if len(combinacionActual) == longitudDeseada:
        combinaciones.append(combinacionActual[:])
        os.system('cls')
        combiCopi = combinaciones[:]
        resultadoGenerarCombinaciones.append(["", "", "", "", "", combiCopi, "", "", "", ""])
        print(tabulate(resultadoGenerarCombinaciones, headersGenerarCombinaciones))
        input("Presione Enter Para Continuar..")
        return
    
    os.system('cls')
    resultadoGenerarCombinaciones.append(["", "", "", "", "", "", "", indiceInicio >= len(puntos), "", ""])
    print(tabulate(resultadoGenerarCombinaciones, headersGenerarCombinaciones))
    input("Presione Enter Para Continuar..")
    if indiceInicio >= len(puntos):
        return

    os.system('cls')
    resultadoGenerarCombinaciones.append(["", "", "", "", "", "", "", "", puntos[indiceInicio], ""])
    print(tabulate(resultadoGenerarCombinaciones, headersGenerarCombinaciones))
    input("Presione Enter Para Continuar..")
    combinacionActual.append(puntos[indiceInicio])
    os.system('cls')
    comActual = combinacionActual[:]
    resultadoGenerarCombinaciones.append(["", "", comActual, "", "", "", "", "", "", ""])
    print(tabulate(resultadoGenerarCombinaciones, headersGenerarCombinaciones))
    input("Presione Enter Para Continuar..")
    
    generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio + 1, combinaciones, i + 1)

    os.system('cls')
    resultadoGenerarCombinaciones.append(["", "", "", "", "", "", "", "", "", True])
    print(tabulate(resultadoGenerarCombinaciones, headersGenerarCombinaciones))
    input("Presione Enter Para Continuar..")
    eliminarUltimoLista(combinacionActual, 0, [])
    os.system('cls')
    comElim = combinacionActual[:]
    resultadoGenerarCombinaciones.append(["", "", comElim, "", "", "", "", "", "", ""])
    print(tabulate(resultadoGenerarCombinaciones, headersGenerarCombinaciones))
    input("Presione Enter Para Continuar..")

    generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio + 1, combinaciones, i + 1)

puntos = [(1, 1), (1, 4), (4, 1), (4, 4)]

def obtenerCombinaciones(puntos, longitudDeseada):
    combinaciones = []
    os.system('cls')
    resultadoObtenerCombinaciones.append([0, puntos, longitudDeseada, []])
    print(tabulate(resultadoObtenerCombinaciones, headersObtenerCombinaciones))
    input("Presione Enter Para Continuar..")
    generarCombinaciones(puntos, [], longitudDeseada, 0, combinaciones)
    os.system('cls')
    resultadoObtenerCombinaciones.append(["", "", "", combinaciones])
    print(tabulate(resultadoObtenerCombinaciones, headersObtenerCombinaciones))
    input("Presione Enter Para Continuar..")
    GenerarText(tabulate(resultadoGenerarCombinaciones, headersGenerarCombinaciones), puntos, "PruebaEscritorioGenerarCombinaciones", combinaciones)
    GenerarText(tabulate(resultadosElimnarUltimo, headersEliminarUltimo), puntos, "PruebaEscritorioEliminarUltimo", combinaciones)
    GenerarText(tabulate(resultadoObtenerCombinaciones, headersObtenerCombinaciones), puntos, "PruebaEscritorioObtenerCombinaciones", combinaciones)
    return combinaciones


obtenerCombinaciones(puntos, 3)