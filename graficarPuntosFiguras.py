import matplotlib.pyplot as plt
from cuadrado import esCuadrado
from rectangulo import esRectangulo
from trianguloRectangulo import esTrianguloRectangulo


# Función para graficar puntos y figuras en un plano cartesiano
def graficarPuntosYFiguras(puntos, titulo):
    x, y = zip(*puntos)  # Separar las coordenadas x e y
    plt.figure()  # Crear una nueva figura para graficar
    plt.scatter(x, y)  # Graficar los puntos en el plano

    # Anotar cada punto con sus coordenadas
    for i, punto in enumerate(puntos):
        plt.annotate(f"{punto}", (x[i], y[i]))

    # Si hay 4 puntos, verificar si forman un cuadrado o rectángulo
    if len(puntos) == 4:
        if esCuadrado(puntos) or esRectangulo(puntos):
            # Ordenar los puntos para dibujar la figura correctamente
            orden = sorted(puntos, key=lambda p: (p[0], p[1]))
            plt.plot(
                [orden[0][0], orden[1][0], orden[3][0], orden[2][0], orden[0][0]],
                [orden[0][1], orden[1][1], orden[3][1], orden[2][1], orden[0][1]],
                "r",
            )
            plt.title(titulo)
    # Si hay 3 puntos, verificar si forman un triángulo rectángulo
    elif len(puntos) == 3 and esTrianguloRectangulo(puntos):
        plt.plot(
            [p[0] for p in list(puntos) + [puntos[0]]],
            [p[1] for p in list(puntos) + [puntos[0]]],
            "g",
        )
        plt.title(titulo)

    # Mostrar la cuadrícula y la figura en la gráfica
    plt.grid(True)
    plt.show()

# Graficar todos los puntos del arrayListas
def graficarTodosLosPuntos(arrayListas):
    plt.figure()
    for lista in arrayListas:
        x, y = zip(*lista)
        plt.scatter(x, y)
        for i, punto in enumerate(lista):
            plt.annotate(f"{punto}", (x[i], y[i]))
    plt.title("Todos los puntos")
    plt.grid(True)
    plt.show()



# alternativa anterios....

# Función recursiva para generar combinaciones de puntos
# def generarCombinaciones(puntos, combinacionActual, longitudDeseada, indiceInicio, combinaciones):
#     # Si la combinación actual tiene la longitud deseada, agregarla a la lista de combinaciones
#     if len(combinacionActual) == longitudDeseada:
#         combinaciones.append(combinacionActual[:]) #combinacionActual[:] -> Agrega una copia de la combinación actual 
#         return
#     # Iterar a partir del índice de inicio para generar combinaciones
#     for i in range(indiceInicio, len(puntos)):
#         combinacionActual.append(puntos[i]) # Agregar el punto actual a la combinación
#         generarCombinaciones(puntos, combinacionActual, longitudDeseada, i + 1, combinaciones) # Llamada recursiva
#         combinacionActual.pop() # Eliminar el último punto para probar otra combinación