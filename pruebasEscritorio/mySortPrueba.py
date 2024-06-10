def quickSortPersonalizado(arreglo):
    print("Arreglo:", arreglo)
    print("len(arreglo) <= 1:", len(arreglo) <= 1)
    input("Enter...")
    if len(arreglo) <= 1:
        print("return:", arreglo)
        return arreglo

    pivote = arreglo[0]
    izquierda = []
    medio = []
    derecha = []

    print("Pivote:", pivote)
    input("Enter...")
    print("izquierda:", izquierda)
    input("Enter...")
    print("medio:", medio)
    input("Enter...")
    print("derecha:", derecha)
    input("Enter...")

    def particion(arreglo, pivote, izquierda, medio, derecha, index=0):
        print(
            "Arreglo:",
            arreglo,
            "pivote:",
            pivote,
            "izquierda:",
            izquierda,
            "medio:",
            medio,
            "derecha:",
            derecha,
            "i:",
            index,
        )
        input("Enter...")
        print("index == len(arreglo):", index == len(arreglo))
        input("Enter...")
        if index == len(arreglo):
            print("izquierda:", izquierda, "medio:", medio, "derecha:", derecha)
            input("Enter...")
            return izquierda, medio, derecha

        print("arreglo[index] < pivote:", arreglo[index] < pivote)
        print("arreglo[index] > pivote:", arreglo[index] > pivote)
        input("Enter...")
        if arreglo[index] < pivote:
            izquierda.append(arreglo[index])
            print("izquierda.append(arreglo[index]):", izquierda)
            input("Enter...")
        elif arreglo[index] > pivote:
            derecha.append(arreglo[index])
            print("derecha.append(arreglo[index]):", derecha)
            input("Enter...")
        else:
            medio.append(arreglo[index])
            print("medio.append(arreglo[index]):", medio)
            input("Enter...")

        print(
            "return -> arreglo:",
            arreglo,
            "pivote:",
            pivote,
            "izquierda:",
            izquierda,
            "medio:",
            medio,
            "derecga:",
            derecha,
            "i:",
            index + 1,
        )
        input("Enter...")
        return particion(arreglo, pivote, izquierda, medio, derecha, index + 1)

    input("Enter...")
    izquierda, medio, derecha = particion(arreglo, pivote, izquierda, medio, derecha)
    print(
        "izquierda, medio, derecha = particion(arreglo, pivote, izquierda, medio, derecha)\n",
        "izquierda:",
        izquierda,
        "medio:",
        medio,
        "derecha:",
        derecha,
    )
    input("Enter...")
    return quickSortPersonalizado(izquierda) + medio + quickSortPersonalizado(derecha)


arreglo = quickSortPersonalizado([3, 6, 8, 10, 1, 2, 1])
print(arreglo)