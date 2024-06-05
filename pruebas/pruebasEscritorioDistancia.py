def calcularDistancia(x1, y1, x2, y2):
  distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
  return distancia

print("Prueba de distancia")
x1 = 1
y1 = 2
x2 = 3
y2 = 4

distancia = calcularDistancia(x1, y1, x2, y2)
print(f"Distancia entre ({x1},{y1}) y ({x2},{y2}): {distancia}")

def calcularDistanciasRecursivo(puntos, i=0, j=1, distancias=None):
  if distancias is None:
    distancias = []

  if i >= len(puntos) - 1:
    return distancias

  if j >= len(puntos):
    return calcularDistanciasRecursivo(puntos, i + 1, i + 2, distancias)

  distancias.append(calcularDistancia(puntos[i][0], puntos[i][1], puntos[j][0], puntos[j][1]))

  return calcularDistanciasRecursivo(puntos, i, j + 1, distancias)

puntos = [(1, 2), (3, 4), (5, 6)]
print("Calculando distancia de n pares de listas")
distancias = calcularDistanciasRecursivo(puntos)
print(distancias)