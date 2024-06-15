def eliminarUltimoLista(lista, i=0, nuevaLista=None):
    if nuevaLista is None:  
        nuevaLista = []

    if i == len(lista) - 1:
        lista[:] = nuevaLista
        return
    
    nuevaLista.append(lista[i])

    eliminarUltimoLista(lista, i + 1, nuevaLista)

def generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio, combinaciones):
    
    if len(combinacionActual) == longitudDeseada:
        combinaciones.append(combinacionActual[:])
        return

    if indiceInicio >= len(puntos):
        return

    combinacionActual.append(puntos[indiceInicio])
    generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio + 1, combinaciones)
    
    # combinacionActual.pop()
    eliminarUltimoLista(combinacionActual)

    generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio + 1, combinaciones)

def obtenerCombinaciones(puntos, longitudDeseada):
    combinaciones = []
    generarCombinaciones(puntos, [], longitudDeseada, 0, combinaciones)
    return combinaciones

