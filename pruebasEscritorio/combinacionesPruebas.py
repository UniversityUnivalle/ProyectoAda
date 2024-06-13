def eliminarUltimoLista(lista, i=0, nuevaLista=None):
    print("Lista:", lista, "i:", i, "nuevaLista:", nuevaLista)
    input("Enter...")
    print("nuevaLista is None:", nuevaLista is None)
    input("Enter...")
    if nuevaLista is None:
        nuevaLista = []
        print("nuevalista:", nuevaLista)
        input("Enter...")

    print("i == len(lista) - 1:", i == len(lista) - 1)
    input("Enter...")
    if i == len(lista) - 1:
        print("lista[:]:", lista[:])
        print("nuevaLista:", nuevaLista)
        input("Enter...")
        lista[:] = nuevaLista
        return

    print("nuevaLista.append(lista[i]):", lista[i])
    input("Enter...")
    nuevaLista.append(lista[i])

    print("Vuelve a llamar la funcion recursivamente...")
    input("Enter...")
    eliminarUltimoLista(lista, i + 1, nuevaLista)


def generarCombinaciones(
    puntos, combinacionActual, longitudDeseada, indiceInicio, combinaciones
):

    print(
        "puntos:",
        puntos,
        "combinacionActual:",
        combinacionActual,
        "longitudDeseada:",
        longitudDeseada,
        "indiceInicio:",
        indiceInicio,
        "combinaciones:",
        combinaciones,
    )
    input("Enter...")
    print(
        "len(combinacionActual) == longitudDeseada:",
        len(combinacionActual) == longitudDeseada,
    )
    input("Enter...")
    if len(combinacionActual) == longitudDeseada:
        print("combinacionActual[:]:", combinacionActual[:])
        input("Enter...")
        combinaciones.append(combinacionActual[:])
        print("combinaciones.append(combinacionActual[:]):", combinaciones)
        input("Enter...")
        return

    print("indiceInicio >= len(puntos):", indiceInicio >= len(puntos))
    if indiceInicio >= len(puntos):
        print("return...")
        input("Enter...")
        return

    print("puntos[indiceInicio]:", puntos[indiceInicio])
    input("Enter...")
    combinacionActual.append(puntos[indiceInicio])
    print("combinacionActual.append(puntos[indiceInicio]):", combinacionActual)
    input("Enter...")
    print(
        "Llamado Recursivo:\npuntos:",
        puntos,
        "combinacionActual:",
        combinacionActual,
        "longitudDeseada:",
        longitudDeseada,
        "indiceInicio:",
        indiceInicio + 1,
        "combinaciones:",
        combinaciones,
    )
    input("Enter..")
    generarCombinaciones(
        puntos, combinacionActual, longitudDeseada, indiceInicio + 1, combinaciones
    )

    print("comnbinaciones:", combinaciones)
    print("Llamado funcion eliminar ultimo:")
    input("Enter...")
    eliminarUltimoLista(combinacionActual)
    print("comnbinaciones eliminado ultimo:", combinaciones)
    input("Enter...")

    print(
        "Llamado Recursivo:\npuntos:",
        puntos,
        "combinacionActual:",
        combinacionActual,
        "longitudDeseada:",
        longitudDeseada,
        "indiceInicio:",
        indiceInicio + 1,
        "combinaciones:",
        combinaciones,
    )
    input("Enter...")
    generarCombinaciones(
        puntos, combinacionActual, longitudDeseada, indiceInicio + 1, combinaciones
    )


puntos = [(1, 1), (1, 4), (4, 1), (4, 4)]


def obtenerCombinaciones(puntos, longitudDeseada):
    print("puntos:", puntos, "longitudDeseada:", longitudDeseada)
    combinaciones = []
    print("combinaciones:", combinaciones)
    generarCombinaciones(puntos, [], longitudDeseada, 0, combinaciones)
    print("combinaciones generadas:", combinaciones)
    return combinaciones


obtenerCombinaciones(puntos, 3)


# def eliminarUltimoLista(lista): #Funcion que va a recibir la lista
#     nuevaLista = [] #Crea una lista nueva

#     for i in range (len(lista) -1): #Recorrer el tamano de la lista menos el ultimo elemento
#         nuevaLista.append(lista [i]) #Cada elemento que se recorre se agrega a la nueva lista

#     lista[:] = nuevaLista #Se modifica la lista original, agregando los elementos de la nueva lista
#                             # = elementos menos el ultimo
