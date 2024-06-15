import time
from tabulate import tabulate
import os

def prueba_de_escritorio(algoritmo, inputs, outputs_esperados):
    """
    Realiza una prueba de escritorio para un algoritmo dado.

    Args:
        algoritmo (func): El algoritmo a probar.
        inputs (list): Lista de entradas para el algoritmo.
        outputs_esperados (list): Lista de salidas esperadas para cada entrada.

    Returns:
        None
    """
    resultados = []
    for i, entrada in enumerate(inputs):
        inicio = time.time()
        salida_real = algoritmo(int(entrada), int(i))
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        resultados.append([f"Entrada {i}", entrada, salida_real, tiempo_ejecucion])
        os.system('cls')
        print(tabulate(resultados, headers=["Entrada", "Input", "Output Real", "Tiempo de Ejecución (s)"]))
        input()
    # print("Resultados de la prueba de escritorio:")
    # tabulado = tabulate(resultados, headers=["Entrada", "Input", "Output Real", "Tiempo de Ejecución (s)"])

# Ejemplo de uso
def suma(a, b):
    return a + b

inputs = [1, 2, 3, 4, 5]
outputs_esperados = [3, 4, 5, 6, 7]

prueba_de_escritorio(suma, inputs, outputs_esperados)