def calcularDistancia(x1, y1, x2, y2):
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distancia

def areaTrianguloRectangulo(puntos):
    base = calcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1])
    altura = calcularDistancia(puntos[0][0], puntos[0][1], puntos[2][0], puntos[2][1])
    return 0.5 * base * altura

# Puntos del triángulo
puntos = [(1, 1), (5, 1), (1, -2)]

# Calcular y mostrar el área
area = areaTrianguloRectangulo(puntos)
print(f"El área del triángulo con puntos {puntos} es {area}")