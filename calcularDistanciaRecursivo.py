# Propósito de la Función
# La función calcularDistancia tiene como objetivo calcular la distancia euclidiana entre dos puntos en un plano cartesiano bidimensional
# Los puntos están definidos por sus coordenadas (x1, y1) (x2, y2).

# La función devuelve la distancia entre los dos puntos

# Parámetros de Entrada
# x1, y1: Coordenadas del primer punto
# x2, y2: Coordenadas del segundo punto

def calcularDistancia(x1, y1, x2, y2):
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distancia


# Se eleva la distancia al cuadrado a la potencia 0.5 por la siguientes razon:
# Equivalencia matemática:
# Elevar un número al cuadrado y luego a la potencia 0.5 es equivalente a calcular su raíz cuadrada. Esto se debe a la propiedad de las potencias:

# (a^n)^m = a^(n*m)
# 
# En este caso, a representa la distancia al cuadrado ((x2 - x1)^2 + (y2 - y1)^2), n es 2 y m es 0.5. Por lo tanto: 

# (a^2)^0.5 = a^(2*0.5) = a

# -------------------------------------
# Propósito:
# calcularDistanciasRecursivo es una función recursiva que calcula todas las distancias entre puntos dados en una lista de puntos

# Parámetros:
# puntos: Lista de puntos. Cada punto está representado por una tupla (x, y)
# i, j: Índices que representan los puntos entre los cuales se está calculando la distancia
# distancias: Lista que almacena las distancias calculadas

# Inicialización:
# distancias = None: Si distancias no se proporciona al llamar la función, se inicializa como una lista vacía

# Condiciones de Terminación:
# i >= len(puntos) - 1: Cuando i es igual o mayor a len(puntos) - 1, significa que se han calculado las distancias para todos los pares posibles de puntos, por lo que la función retorna distancias
# j >= len(puntos): Cuando j es igual o mayor a len(puntos), se pasa al siguiente punto en i y se reinicia j a i + 2 para evitar calcular la distancia entre un punto y sí mismo y para evitar duplicados

# Cálculo de Distancia:
# distancias.append(...): Calcula la distancia entre los puntos puntos[i] y puntos[j] utilizando la función calcularDistancia, y añade el resultado a la lista distancias

# Llamada Recursiva:
# return calcularDistanciasRecursivo(puntos, i, j + 1, distancias): Llama recursivamente a la función con j incrementado en 1 para calcular la siguiente distancia

def calcularDistanciasRecursivo(puntos, i=0, j=1, distancias=None):
    if distancias is None:
        distancias = []

    if i >= len(puntos) - 1:
        return distancias

    if j >= len(puntos):
        return calcularDistanciasRecursivo(puntos, i + 1, i + 2, distancias)

    distancias.append(calcularDistancia(puntos[i][0], puntos[i][1], puntos[j][0], puntos[j][1]))

    return calcularDistanciasRecursivo(puntos, i, j + 1, distancias)