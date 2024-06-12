def calcularDistancia(x1, y1, x2, y2):
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distancia

def calcularDistanciasRecursivo(puntos, i=0, j=1, distancias=None):
    if distancias is None:
        distancias = []

    if i >= len(puntos) - 1:
        return distancias

    if j >= len(puntos):
        return calcularDistanciasRecursivo(puntos, i + 1, i + 2, distancias)

    distancias.append(calcularDistancia(puntos[i][0], puntos[i][1], puntos[j][0], puntos[j][1]))

    return calcularDistanciasRecursivo(puntos, i, j + 1, distancias)
#----------------------------------------------------------------------------------------------------#


def areaCuadrado(puntos):
    lado = calcularDistancia(puntos[0][0], puntos[0][1], puntos[1][0], puntos[1][1])
    return lado * lado

def esCuadrado(puntos):
    if len(puntos) != 4:
        return False

    print("\nVerificando si los puntos forman un cuadrado")
    print("Puntos:", puntos)
    input("Presiona Enter para continuar...")

    distancias = calcularDistanciasRecursivo(puntos)

    print("\nDistancias calculadas:")
    print(distancias)
    input("Presiona Enter para continuar...")

    distancias.sort()
    print("\nDistancias ordenadas:")
    print(distancias)
    input("Presiona Enter para continuar...")

    es_cuadrado = (distancias[0] == distancias[1] == distancias[2] == distancias[3] and 
                   distancias[4] == distancias[5])

    if es_cuadrado:
        print("\n¡Los puntos forman un cuadrado!")
    else:
        print("\nLos puntos NO forman un cuadrado")

    return es_cuadrado

# Ejemplo de uso
puntos = [(0, 0), (0, 1), (1, 0), (1, 1)]
print(f"\nVerificando si los puntos forman un cuadrado: {puntos}")
es_cuadrado = esCuadrado(puntos)
print(f"¿Los puntos forman un cuadrado?: {es_cuadrado}")
