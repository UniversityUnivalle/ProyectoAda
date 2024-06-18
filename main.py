from instalacionDependencias.dependencias import Install_Dependencies

Install_Dependencies()

from verificarListas import verificarListas
from trianguloRectangulo import esTrianguloRectangulo, areaTrianguloRectangulo
from cuadrado import esCuadrado, areaCuadrado
from rectangulo import esRectangulo, areaRectangulo
from combinaciones import obtenerCombinaciones
from graficarPuntosFiguras import graficarTodosLosPuntos, procesarFigura, graficarTodasLasFiguras
from arbol import arbolFiguras

arrayListas = [
    # [(1, 1), (1, 5), (5, 1), (1, -2), (5, -2)]
    # [(1, 1), (1, 2), (2, 1), (2, 2)],
    # [(2, 1), (1, 2), (2, 3), (3, 2)],
    # [(1, 2), (2, 4), (4, 3), (3, 1)],
    # [(3, 20), (14, 9), (4, 5), (3, 2), (15, 2), (24, -5), (7, -5), (-4, -5), (7, -24)],
    # [(0, 0), (3, 0), (0, 4), (0, 3), (5, 3), (5, 0), (0, 2), (2, 2), (2, 0)]
    [(2, 0), (0, 4), (2, 2), (0, 2)]
    
]

# Verificar las listas
listasValidas = verificarListas(arrayListas)

triangulosRectangulos = []
cuadrados = []
rectangulos = []
todasLasFiguras = []

for lista in listasValidas:
    combinaciones = []
    
    # Generar combinaciones de 3 y 4 puntos
    for longitudDeseada in range(3, 5):
        combinaciones += obtenerCombinaciones(lista, longitudDeseada)

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

print("-----------------------------------------------------------------")
print("Imprimiendo árbol de figuras:")
arbolFiguras.imprimirArbol()

graficarTodosLosPuntos(arrayListas)

graficarTodasLasFiguras(todasLasFiguras, "Todas las Figuras")

arbolFiguras.graficarArbol()

# Imprimir el conteo de figuras encontradas
print("-----------------------------------------------------------------")
print(f"Triángulos rectángulos encontrados: {len(triangulosRectangulos)}")
print(f"Cuadrados encontrados: {len(cuadrados)}")
print(f"Rectángulos encontrados: {len(rectangulos)}")
print("-----------------------------------------------------------------")


