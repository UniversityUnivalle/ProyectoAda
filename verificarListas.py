def verificarListas(arrayListas):
    listasValidas = []
    for lista in arrayListas:
        if len(lista) >= 3:
            listasValidas.append(lista)
        else:
            print(f"Lista {lista} no tiene suficientes puntos.")
    return listasValidas
