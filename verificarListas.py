# Propósito:
# La función verificarListas toma como entrada una lista de listas (arrayListas) y devuelve una lista filtrada (listasValidas)
# que contiene solo las listas que tienen tres o más elementos

# Parámetros:
# arrayListas: Lista de listas. Cada lista representa una colección de elementos

# Variables:
# listasValidas: Lista que almacena las listas válidas que cumplen con el criterio (tienen al menos 3 elementos)

# Iteración y Filtrado:
# for lista in arrayListas:
# Itera sobre cada lista dentro de arrayListas.
# if len(lista) >= 3:
# Verifica si la longitud (len(lista)) de la lista actual (lista) es mayor o igual a 3.
# Si es verdadero, agrega la lista a listasValidas utilizando listasValidas.append(lista)
# else:
# Si la lista no tiene al menos 3 elementos, imprime un mensaje indicando que la lista no tiene suficientes puntos (print(f"Lista {lista} no tiene suficientes puntos."))

# Retorno:
# return listasValidas
# Devuelve la lista listasValidas, que contiene todas las listas de arrayListas que tienen al menos 3 elementos

def verificarListas(arrayListas):
    listasValidas = []
    for lista in arrayListas:
        if len(lista) >= 3:
            listasValidas.append(lista)
        else:
            print(f"Lista {lista} no tiene suficientes puntos.")
    return listasValidas
