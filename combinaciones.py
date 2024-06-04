def generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio, combinaciones):
    
    if len(combinacionActual) == longitudDeseada:
        combinaciones.append(combinacionActual[:])
        return

    if indiceInicio >= len(puntos):
        return

    combinacionActual.append(puntos[indiceInicio])
    generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio + 1, combinaciones)
    
    combinacionActual.pop()
    generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio + 1, combinaciones)

def obtenerCombinaciones(puntos, longitudDeseada):
    combinaciones = []
    generarCombinaciones(puntos, [], longitudDeseada, 0, combinaciones)
    return combinaciones