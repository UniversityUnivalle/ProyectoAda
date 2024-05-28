from calcularDistanciaRecursivo import calcularDistanciasRecursivo,calcularDistancia


# Propósito:
# areaCuadrado calcula el área de un cuadrado dado los puntos que definen dos de sus lados adyacentes

# Parámetros:
# puntos: Lista de puntos que definen los vértices del cuadrado

# Cálculo del Área:
# lado = calcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1]): Calcula la distancia entre el primer y segundo punto
# para obtener la longitud de uno de los lados del cuadrado
# return lado * lado: Retorna el área del cuadrado, que es el lado al cuadrado
def areaCuadrado(puntos):
    lado = calcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1])
    return lado * lado


# Propósito:
# esCuadrado verifica si los puntos dados forman un cuadrado, es decir, si todas las distancias entre los vértices son iguales

# Parámetros:
# puntos: Lista de puntos que definen los vértices del cuadrado

# Verificación:
# if len(puntos) != 4:: Si la cantidad de puntos no es igual a 4, retorna False porque no se puede formar un cuadrado con más o menos de cuatro puntos
# distancias = calcularDistanciasRecursivo(puntos): Calcula todas las distancias entre los puntos utilizando la función calcularDistanciasRecursivo
# distancias.sort(): Ordena las distancias de menor a mayor
# return distancias[0] == distancias[1] == distancias[2] == distancias[3]: Retorna True si todas las distancias son iguales, lo cual indica que los puntos forman un cuadrado
def esCuadrado(puntos):
    if len(puntos) != 4:
        return False

    distancias = calcularDistanciasRecursivo(puntos)

    distancias.sort()
    return distancias[0] == distancias[1] == distancias[2] == distancias[3]
