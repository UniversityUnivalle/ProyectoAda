import matplotlib.pyplot as plt
import numpy as np
from verificarListas import verificarListas
from calcularDistanciaListas import recorrerLista

arrayListas = [
[[0, 0], [2, 0], [1, 1], [1, -1]]
    
]

# Verificar las listas
listasValidas = verificarListas(arrayListas)

# Recorrer cada lista válida y calcular las distancias
for lista in listasValidas:
    recorrerLista(0, lista)
