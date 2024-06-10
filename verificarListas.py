def verificarListas(arrayListas, i=0, listasValidas=None):
    if listasValidas is None:
        listasValidas = []

    if i >= len(arrayListas):
        return listasValidas

    lista = arrayListas[i]

    if len(lista) >= 3:
        listasValidas.append(lista)
    else:
        print(f"Lista {lista} no tiene suficientes puntos.")

    return verificarListas(arrayListas, i + 1, listasValidas)