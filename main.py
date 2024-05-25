import matplotlib.pyplot as plt
from verificarListas import verificarListas
from trianguloRectangulo import esTrianguloRectangulo,areaTrianguloRectangulo
from cuadrado import esCuadrado,areaCuadrado
from rectangulo import esRectangulo,areaRectangulo
from combinaciones import obtenerCombinaciones
from graficarPuntosFiguras import graficarPuntosYFiguras,graficarTodosLosPuntos
from arbol import agregarFiguraAlArbol,arbolFiguras

arrayListas = [
    [(1, 1), (1, 5), (5, 1), (1, -2), (5, -2)],
    [(3, 20), (1, 9), (4, 5), (3, 2), (15, 2), (-4, 0), (7, -5)],
    [(1, 1), (1, 4), (4, 1), (4, 4)],
    [(1, 0), (3, 5)]
]

# Verificar las listas
listasValidas = verificarListas(arrayListas)

# Arreglo para almacenar las figuras con sus áreas
figuras = []

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
                area = areaCuadrado(comb)
                figura = {
                    "identificador": f"Cuadrado_{len(figuras)+1}",
                    "tipo": "Cuadrado",
                    "puntos": comb,
                    "area": area
                }
                cuadrados.append(figura)
                figuras.append(figura)
                agregarFiguraAlArbol(figura,arbolFiguras)
                print(f"Los puntos {comb} forman un cuadrado con área {area}.")
                graficarPuntosYFiguras(comb, "Cuadrado")
                agregarFiguraAlArbol(figura,arbolFiguras)
            elif esRectangulo(comb):
                area = areaRectangulo(comb)
                figura = {
                    "identificador": f"Rectángulo_{len(figuras)+1}",
                    "tipo": "Rectángulo",
                    "puntos": comb,
                    "area": area
                }
                rectangulos.append(figura)
                figuras.append(figura)
                agregarFiguraAlArbol(figura,arbolFiguras)
                print(f"Los puntos {comb} forman un rectángulo con área {area}.")
                graficarPuntosYFiguras(comb, "Rectángulo")
        elif len(comb) == 3 and esTrianguloRectangulo(comb):
            area = areaTrianguloRectangulo(comb)
            figura = {
                "identificador": f"TriánguloRectángulo_{len(figuras)+1}",
                "tipo": "Triángulo Rectángulo",
                "puntos": comb,
                "area": area
            }
            triangulosRectangulos.append(figura)
            figuras.append(figura)
            print(f"Los puntos {comb} forman un triángulo rectángulo con área {area}.")
            graficarPuntosYFiguras(comb, "Triángulo Rectángulo")
            agregarFiguraAlArbol(figura,arbolFiguras)
        else:
            print(f"Los puntos {comb} no forman una figura específica.")

# Imprimir las figuras encontradas y sus áreas
for figura in figuras:
    print(f"Figura: {figura['identificador']}, Tipo: {figura['tipo']}, Puntos: {figura['puntos']}, Área: {figura['area']}")

print("imprimiendo arbol")
# Imprimir el árbol de figuras
arbolFiguras.imprimirArbol()

# Grafica todos los puntos existentes del arrayListas
graficarTodosLosPuntos(arrayListas)

# Imprimir el conteo de figuras encontradas
print(f"Triángulos rectángulos encontrados: {len(triangulosRectangulos)}")
print(f"Cuadrados encontrados: {len(cuadrados)}")
print(f"Rectángulos encontrados: {len(rectangulos)}")
