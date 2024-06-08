# def verificarListas(arrayListas):
#     listasValidas = []
#     for lista in arrayListas:
#         if len(lista) >= 3:
#             listasValidas.append(lista)
#         else:
#             print(f"Lista {lista} no tiene suficientes puntos.")
#     return listasValidas

def verificarListas(arrayListas):
    listasValidas = []

    i = 0
    while i < len(arrayListas):
        lista = arrayListas[i]

        if len(lista) >= 3:
            listasValidas.append(lista)
        else:
            print(f"Lista {lista} no tiene suficientes puntos.")

        i += 1

    return listasValidas