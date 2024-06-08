from verificarListas import verificarListas
from trianguloRectangulo import esTrianguloRectangulo, areaTrianguloRectangulo
from cuadrado import esCuadrado, areaCuadrado
from rectangulo import esRectangulo, areaRectangulo
from combinaciones import obtenerCombinaciones
from graficarPuntosFiguras import graficarTodosLosPuntos,procesarFigura
from arbol import arbolFiguras

arrayListas = [
    [(1, 1), (1, 4), (4, 1), (4, 4)],
    [(1,2), (3,2)]
]

# Verificar las listas
listasValidas = verificarListas(arrayListas)

# Arreglos para almacenar las figuras encontradas
triangulosRectangulos = []
cuadrados = []
rectangulos = []


# Para cada lista válida de puntos
for lista in listasValidas:
    combinaciones = []
    
    # Generar combinaciones de 3 y 4 puntos
    for r in range(3, 5):
        combinaciones += obtenerCombinaciones(lista, r)

    # Verificar cada combinación generada
    for comb in combinaciones:
        if len(comb) == 4:
            if esCuadrado(comb):
                procesarFigura("Cuadrado", comb, areaCuadrado(comb), cuadrados)
            elif esRectangulo(comb):
                procesarFigura("Rectángulo", comb, areaRectangulo(comb), rectangulos)
        elif len(comb) == 3 and esTrianguloRectangulo(comb):
            procesarFigura("Triángulo Rectángulo", comb, areaTrianguloRectangulo(comb), triangulosRectangulos)
        else:
            print(f"Los puntos {comb} no forman una figura específica.")

# Imprimir las figuras encontradas y sus áreas
for figura in triangulosRectangulos + cuadrados + rectangulos:
    print(f"Figura: {figura['identificador']}, Tipo: {figura['tipo']}, Puntos: {figura['puntos']}, Área: {figura['area']}")

print("Imprimiendo árbol de figuras:")
# Imprimir el árbol de figuras
arbolFiguras.imprimirArbol()

# Graficar todos los puntos existentes del arrayListas
graficarTodosLosPuntos(arrayListas)

# Imprimir el conteo de figuras encontradas
print(f"Triángulos rectángulos encontrados: {len(triangulosRectangulos)}")
print(f"Cuadrados encontrados: {len(cuadrados)}")
print(f"Rectángulos encontrados: {len(rectangulos)}")
