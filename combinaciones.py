def generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio, combinaciones):
    
    if len(combinacionActual) == longitudDeseada:
        combinaciones.append(combinacionActual[:])
        return

    if indiceInicio >= len(puntos):
        return

    combinacionActual.append(puntos[indiceInicio])
    generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio + 1, combinaciones)
    
    eliminarUltimoLista(combinacionActual)
    generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio + 1, combinaciones)

def obtenerCombinaciones(puntos, longitudDeseada):
    combinaciones = []
    generarCombinaciones(puntos, [], longitudDeseada, 0, combinaciones)
    return combinaciones


def eliminarUltimoLista(lista): #Funcion que va a recibir la lista
    nuevaLista = [] #Crea una lista nueva

    for i in range (len(lista) -1): #Recorrer el tamano de la lista menos el ultimo elemento
        nuevaLista.append(lista [i]) #Cada elemento que se recorre se agrega a la nueva lista

    lista[:] = nuevaLista #Se modifica la lista original, agregando los elementos de la nueva lista 
                            # = elementos menos el ultimo



    # mi_lista = [1,2,3,4,5]
    # mi_lista = mi_lista[:-1]
    # print(mi_lista)