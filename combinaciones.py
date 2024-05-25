def generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio, combinaciones):
    # Si la combinación actual tiene la longitud deseada, agregarla a la lista de combinaciones
    if len(combinacionActual) == longitudDeseada:
        combinaciones.append(combinacionActual[:])  # Agrega una copia de la combinación actual
        return

    # Condición de salida si el índice de inicio excede la longitud de los puntos
    if indiceInicio >= len(puntos):
        return

    # Incluir el punto actual en la combinación y llamar recursivamente
    combinacionActual.append(puntos[indiceInicio])
    generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio + 1, combinaciones)
    
    # Excluir el punto actual de la combinación y llamar recursivamente
    combinacionActual.pop()
    generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio + 1, combinaciones)


# Función para obtener todas las combinaciones de una longitud dada
def obtenerCombinaciones(puntos, longitudDeseada):
    combinaciones = []
    generarCombinaciones(puntos, [], longitudDeseada, 0, combinaciones)
    return combinaciones