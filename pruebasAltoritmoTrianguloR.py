import itertools
import matplotlib.pyplot as plt

# Función para verificar si tres puntos son colineales
def sonColineales(p1, p2, p3):
    # Verifica si el área del triángulo formado por los tres puntos es cero (indicador de colinealidad)
    return (p3[1] - p1[1]) * (p2[0] - p1[0]) == (p2[1] - p1[1]) * (p3[0] - p1[0])

# Función para calcular la distancia entre dos puntos
def distancia(p1, p2):
    # Utiliza la fórmula de distancia euclidiana entre dos puntos
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

# Función para verificar si un triángulo es rectángulo
def esTrianguloR(p1, p2, p3):
    # Calcula las distancias entre los tres pares de puntos y las ordena
    lados = sorted([distancia(p1, p2), distancia(p2, p3), distancia(p3, p1)])
    # Verifica si se cumple el teorema de Pitágoras con una tolerancia pequeña para manejar errores de precisión
    return abs(lados[2]**2 - (lados[0]**2 + lados[1]**2)) < 0.000000001 #1×10^-9 o -> 1e-9

# Lista de puntos en el plano cartesiano
puntos = [(1, 1), (1, 5), (5, 1), (1, -2), (5, -2)]

# Generar todas las combinaciones posibles de tres puntos
combinaciones = list(itertools.combinations(puntos, 3))

# Listas para almacenar triángulos válidos y triángulos rectángulos
triangulos = []
triangulosR = []

# Iterar sobre todas las combinaciones de tres puntos
for comb in combinaciones:
    # Si los puntos no son colineales, forman un triángulo válido
    if not sonColineales(*comb):
        triangulos.append(comb)
        # Si el triángulo es rectángulo, se añade a la lista correspondiente
        if esTrianguloR(*comb):
            triangulosR.append(comb)

# Mostrar los triángulos encontrados
print("Triángulos encontrados:")
for t in triangulos:
    print(t)

print("\nTriángulos rectángulos encontrados:")
for tr in triangulosR:
    print(tr)

# Graficar los triángulos
plt.figure(figsize=(8, 6))
for t in triangulos:
    # Añadir el primer punto al final para cerrar el triángulo en la gráfica
    t = list(t) + [t[0]]
    # Extraer las coordenadas x e y de los puntos
    x, y = zip(*t)
    # Graficar el triángulo
    plt.plot(x, y, marker='o')

# Señalar y etiquetar los puntos en la gráfica
for p in puntos:
    plt.scatter(p[0], p[1], color='red')  # Marca los puntos en rojo
    plt.text(p[0], p[1], f'({p[0]},{p[1]})', fontsize=12, ha='right')  # Etiqueta los puntos

# Configuraciones de la gráfica
plt.title("Triángulos en el plano cartesiano")
plt.xlabel("X")
plt.ylabel("Y")
# Líneas del eje
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
# Cuadrícula
plt.grid(color='gray', linestyle='--', linewidth=0.5)
# Mostrar la gráfica
plt.show()
