from calcularDistanciaRecursivo import calcularDistanciasRecursivo,calcularDistancia


# Propósito:
# areaTrianguloRectangulo calcula el área de un triángulo rectángulo dado los puntos que definen sus vértices

# Parámetros:
# puntos: Lista de puntos que definen los vértices del triángulo rectángulo

# Cálculo del Área:
# base = calcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1]): Calcula la distancia entre el primer y segundo punto para obtener la base del triángulo
# altura = calcularDistancia(puntos[0][0], puntos[0][1], puntos[2][0], puntos[2][1]): Calcula la distancia entre el primer y tercer punto para obtener la altura del triángulo
# return 0.5 * base * altura: Retorna el área del triángulo rectángulo, que es la mitad del producto de la base por la altura.
def areaTrianguloRectangulo(puntos):
    base = calcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1])
    altura = calcularDistancia(puntos[0][0], puntos[0][1], puntos[2][0], puntos[2][1])
    return 0.5 * base * altura

# Propósito:
# elevarDistanciasCuadrado es una función recursiva que eleva al cuadrado cada elemento de la lista distancias

# Parámetros:
# distancias: Lista de números (distancias entre los puntos)
# index: Índice actual para recorrer la lista de distancias

# Recursión:
# if index >= len(distancias):: Condición de salida de la recursión
# distancias[index] = distancias[index] ** 2: Eleva al cuadrado el elemento en la posición index
# return elevarDistanciasCuadrado(distancias, index + 1): Llamada recursiva para procesar el siguiente elemento

# Retorno:
# Retorna la lista distancias con todos sus elementos elevados al cuadrado
def elevarDistanciasCuadrado(distancias, index=0):
    if index >= len(distancias):
        return distancias
    distancias[index] = distancias[index] ** 2
    return elevarDistanciasCuadrado(distancias, index + 1)


# Propósito:
# esTrianguloRectangulo verifica si los puntos dados forman un triángulo rectángulo utilizando el teorema de Pitágoras.

# Parámetros:
# puntos: Lista de puntos que definen los vértices del triángulo

# Verificación:
# if len(puntos) != 3:: Si la cantidad de puntos no es igual a 3, retorna False porque no se puede formar un triángulo rectángulo con más o menos de tres puntos
# distancias = calcularDistanciasRecursivo(puntos): Calcula todas las distancias entre los puntos utilizando la función calcularDistanciasRecursivo
# distancias = elevarDistanciasCuadrado(distancias): Eleva al cuadrado todas las distancias utilizando la función elevarDistanciasCuadrado
# distancias.sort(): Ordena las distancias de menor a mayor
# return distancias[0] + distancias[1] == distancias[2]: Retorna True si las dos distancias más cortas (los dos primeros elementos después de ordenar)
# elevadas al cuadrado suman igual a la distancia más larga (el tercer elemento después de ordenar), lo que indica que el triángulo es rectángulo según el teorema de Pitágoras
def esTrianguloRectangulo(puntos):
    if len(puntos) != 3:
        return False

    distancias = calcularDistanciasRecursivo(puntos)
    distancias = elevarDistanciasCuadrado(distancias)

    distancias.sort()
    return distancias[0] + distancias[1] == distancias[2]
