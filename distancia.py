# Propósito de la Función
# La función calcularDistancia tiene como objetivo calcular la distancia euclidiana entre dos puntos en un plano cartesiano bidimensional.
# Los puntos están definidos por sus coordenadas (x1, y1) (x2, y2).

# La función devuelve la distancia entre los dos puntos.

# Parámetros de Entrada
# x1, y1: Coordenadas del primer punto.
# x2, y2: Coordenadas del segundo punto.

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

