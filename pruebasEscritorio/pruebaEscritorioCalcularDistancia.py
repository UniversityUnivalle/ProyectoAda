enter = "Presiona Enter para continuar..."

def calcularDistancia(x1, y1, x2, y2):
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distancia

def calcularDistanciasRecursivo(puntos, i=0, j=1, distancias=None):
    if distancias is None:
        distancias = []

    print(f"\nLlamada recursiva: i = {i}, j = {j}")
    print(f"Puntos: {puntos}")
    print(f"Distancias acumuladas hasta ahora: {distancias}")
    input(enter)

    if i >= len(puntos) - 1:
        print(f"i ({i}) >= len(puntos) - 1 ({len(puntos) - 1})")
        print(f"Retornando distancias acumuladas: {distancias}")
        input(enter)
        return distancias

    if j >= len(puntos):
        print(f"j ({j}) >= len(puntos) ({len(puntos)})")
        print(f"Siguiente iteración: i = {i + 1}, j = {i + 2}")
        input(enter)
        return calcularDistanciasRecursivo(puntos, i + 1, i + 2, distancias)

    punto1 = puntos[i]
    punto2 = puntos[j]
    distancia = calcularDistancia(punto1[0], punto1[1], punto2[0], punto2[1])
    distancias.append(distancia)

    print(f"Calculando distancia entre {punto1} y {punto2}")
    print(f"Distancia calculada: {distancia}")
    print(f"Distancias acumuladas: {distancias}")
    input(enter)

    return calcularDistanciasRecursivo(puntos, i, j + 1, distancias)

# Ejemplo de uso
puntos = [(0, 0), (3, 4), (6, 8), (9, 12)]
print(f"\nCalculando distancias para los puntos: {puntos}")
distancias = calcularDistanciasRecursivo(puntos)
print(f"\nDistancias finales calculadas: {distancias}")
