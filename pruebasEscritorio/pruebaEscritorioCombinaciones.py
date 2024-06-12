def generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio, combinaciones, iterador=0):
    print(f"Iterador {iterador}: generarCombinaciones(puntos={puntos}, combinacionActual={combinacionActual}, longitudDeseada={longitudDeseada}, indiceInicio={indiceInicio}, combinaciones={combinaciones})")
    input("Enter para continuar...")

    if len(combinacionActual) == longitudDeseada:
        print(f"Iterador {iterador}: Longitud de combinacionActual alcanzada, añadiendo a combinaciones.")
        combinaciones.append(combinacionActual[:])
        input("Enter para continuar...")
        return

    if indiceInicio >= len(puntos):
        print(f"Iterador {iterador}: Índice de inicio mayor o igual a la longitud de puntos, retornando.")
        input("Enter para continuar...")
        return

    combinacionActual.append(puntos[indiceInicio])
    print(f"Iterador {iterador}: Añadido punto {puntos[indiceInicio]} a combinacionActual: {combinacionActual}")
    input("Enter para continuar...")

    generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio + 1, combinaciones, iterador + 1)
    print(f"Iterador {iterador}: Llamada recursiva con combinacionActual: {combinacionActual}")
    input("Enter para continuar...")

    # combinacionActual.pop()
    eliminarUltimoLista(combinacionActual)
    print(f"Iterador {iterador}: Eliminado último elemento de combinacionActual: {combinacionActual}")
    input("Enter para continuar...")

    generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio + 1, combinaciones, iterador + 2)
    print(f"Iterador {iterador}: Llamada recursiva después de eliminar último elemento: {combinacionActual}")
    input("Enter para continuar...")

def obtenerCombinaciones(puntos, longitudDeseada):
    combinaciones = []
    generarCombinaciones(puntos, [], longitudDeseada, 0, combinaciones)
    return combinaciones

def eliminarUltimoLista(lista, i=0, nuevaLista=None):
    if nuevaLista is None:
        nuevaLista = []

    if i == len(lista) - 1:
        lista[:] = nuevaLista
        return
    
    nuevaLista.append(lista[i])
    eliminarUltimoLista(lista, i + 1, nuevaLista)

# Ejemplo de uso
# puntos = [(2, 3), (1, 0), (1, 3), (9, 9)]
puntos = [ 'A', 'B', 'C', 'D']
longitudDeseada = 2
combinaciones = obtenerCombinaciones(puntos, longitudDeseada)
print("Combinaciones obtenidas:", combinaciones)
