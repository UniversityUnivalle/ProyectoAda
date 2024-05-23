from distancia import calcularDistancia

def calcularDistanciasLista(j: int, i: int, lista: list):
    if j < len(lista):
        if j != i:
            print(
                lista[i],
                lista[j],
                calcularDistancia(lista[i][0], lista[j][0], lista[i][1], lista[j][1]),
            )
            calcularDistanciasLista(j + 1, i, lista)
        else:
            calcularDistanciasLista(j + 1, i, lista)

def recorrerLista(i, lista):
    if i < len(lista):
        calcularDistanciasLista(0, i, lista)
        recorrerLista(i + 1, lista)
