def verificarListas(arrayListas, i=0, listasValidas=None):
    print("Inicio de la función")
    print("arrayListas:", arrayListas)
    print("i:", i)
    print("listasValidas:", listasValidas)
    input("Enter...")

    if listasValidas is None:
        listasValidas = []
        print("Inicializando listasValidas a lista vacía.")
        input("Enter...")

    print("i >= len(arrayListas):", i >= len(arrayListas))
    input("Enter...")
    if i >= len(arrayListas):
        print("Retornando listasValidas:", listasValidas)
        return listasValidas

    lista = arrayListas[i]
    print("lista actual:", lista)
    input("Enter...")

    print("len(lista) >= 3:", len(lista) >= 3)
    input("Enter...")
    if len(lista) >= 3:
        listasValidas.append(lista)
        print("Añadiendo lista a listasValidas:", listasValidas)
        input("Enter...")
    else:
        print(f"La lista {lista} no tiene suficientes puntos.")
        input("Enter...")

    print("Llamada recursiva: verificarListas(arrayListas, i + 1, listasValidas)")
    input("Enter...")
    return verificarListas(arrayListas, i + 1, listasValidas)

# Ejemplo de prueba
arrayListas = [[1, 2], [3, 4, 5], [6, 7, 8, 9], [10]]
print("Resultado final:", verificarListas(arrayListas))
