from distancia import calcularDistancia
from calcularDistanciaRecursivo import calcularDistanciasRecursivo


# Propósito:
# areaRectangulo calcula el área de un rectángulo a partir de los puntos dados.

# Parámetros:
# puntos: Lista de puntos que definen los vértices del rectángulo.

# Cálculo del Área:
# lado1 = calcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1]): Calcula la distancia entre los primeros dos puntos para obtener el primer lado del rectángulo.
# lado2 = calcularDistancia(puntos[1][0], puntos[1][1], puntos[2][0], puntos[2][1]): Calcula la distancia entre el segundo y tercer punto para obtener el segundo lado del rectángulo.
# return lado1 * lado2: Retorna el área del rectángulo, que es el producto de los dos lados calculados.
def areaRectangulo(puntos):
    lado1 = calcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1])
    lado2 = calcularDistancia(puntos[1][0], puntos[1][1], puntos[2][0], puntos[2][1])
    return lado1 * lado2


# Propósito:
# esRectangulo verifica si los puntos dados forman un rectángulo.

# Parámetros:
# puntos: Lista de puntos que definen los vértices del cuadrilátero.

# Verificación:
# if len(puntos) != 4:: Si la cantidad de puntos no es igual a 4, retorna False porque no se puede formar un rectángulo con menos o más de cuatro puntos.
# distancias = calcularDistanciasRecursivo(puntos): Calcula todas las distancias entre los puntos utilizando la función calcularDistanciasRecursivo.
# distancias.sort(): Ordena las distancias de menor a mayor.
# return distancias[0] == distancias[1] and distancias[2] == distancias[3]: Retorna True si las distancias más cortas 
# (los dos primeros y los dos últimos elementos de distancias después de ordenar) son iguales, lo que indica que el cuadrilátero es un rectángulo.
def esRectangulo(puntos):
    if len(puntos) != 4:
        return False

    distancias = calcularDistanciasRecursivo(puntos)

    distancias.sort()
    return distancias[0] == distancias[1] and distancias[2] == distancias[3]
