from verificarListas import verificarListas
from trianguloRectangulo import esTrianguloRectangulo, areaTrianguloRectangulo
from cuadrado import esCuadrado, areaCuadrado
from rectangulo import esRectangulo, areaRectangulo
from combinaciones import obtenerCombinaciones
from graficarPuntosFiguras import graficarTodosLosPuntos, procesarFigura, graficarTodasLasFiguras
from arbol import arbolFiguras

arrayListas = [
    [(1, 1), (1, 5), (5, 1), (1, -2), (5, -2)],
    [(1, 1), (1, 2), (2, 1), (2, 2)],
    [(2, 1), (1, 2), (2, 3), (3, 2)],
    [(1, 2), (2, 4), (4, 3), (3, 1)]
]

# Verificar las listas
listasValidas = verificarListas(arrayListas)

# Arreglos para almacenar las figuras encontradas
triangulosRectangulos = []
cuadrados = []
rectangulos = []
todasLasFiguras = []

# Para cada lista válida de puntos
for lista in listasValidas:
    combinaciones = []
    
    # Generar combinaciones de 3 y 4 puntos
    for longitudDeseada in range(3, 5):
        combinaciones += obtenerCombinaciones(lista, longitudDeseada)

    # Verificar cada combinación generada
    for comb in combinaciones:
        if len(comb) == 4:
            if esCuadrado(comb):
                procesarFigura("Cuadrado", comb, areaCuadrado(comb), cuadrados, todasLasFiguras)
            elif esRectangulo(comb):
                procesarFigura("Rectángulo", comb, areaRectangulo(comb), rectangulos, todasLasFiguras)
        elif len(comb) == 3 and esTrianguloRectangulo(comb):
            procesarFigura("Triángulo Rectángulo", comb, areaTrianguloRectangulo(comb), triangulosRectangulos, todasLasFiguras)
        else:
            print(f"Los puntos {comb} no forman una figura específica.")

# # Imprimir las figuras encontradas y sus áreas
# for figura in triangulosRectangulos + cuadrados + rectangulos:
#     print(f"Figura: {figura['identificador']}, Tipo: {figura['tipo']}, Puntos: {figura['puntos']}, Área: {figura['area']}")

print("-----------------------------------------------------------------")
print("Imprimiendo árbol de figuras:")
# Imprimir el árbol de figuras
arbolFiguras.imprimirArbol()

# Graficar todos los puntos existentes del arrayListas
graficarTodosLosPuntos(arrayListas)

# Graficar todas las figuras encontradas
graficarTodasLasFiguras(todasLasFiguras, "Todas las Figuras")

# Graficar el árbol de figuras
arbolFiguras.graficarArbol()

# Imprimir el conteo de figuras encontradas
print("-----------------------------------------------------------------")
print(f"Triángulos rectángulos encontrados: {len(triangulosRectangulos)}")
print(f"Cuadrados encontrados: {len(cuadrados)}")
print(f"Rectángulos encontrados: {len(rectangulos)}")
print("-----------------------------------------------------------------")


