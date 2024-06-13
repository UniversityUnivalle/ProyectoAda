enter = "Presiona Enter para continuar..."


def quickSortPersonalizado(arreglo):
    print("Arreglo:", arreglo)
    print("len(arreglo) <= 1:", len(arreglo) <= 1)
    input(enter)
    if len(arreglo) <= 1:
        print("return:", arreglo)
        return arreglo

    pivote = arreglo[0]
    izquierda = []
    medio = []
    derecha = []

    print("Pivote:", pivote)
    input(enter)
    print("izquierda:", izquierda)
    input(enter)
    print("medio:", medio)
    input(enter)
    print("derecha:", derecha)
    input(enter)

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
        input(enter)
        print("index == len(arreglo):", index == len(arreglo))
        input(enter)
        if index == len(arreglo):
            print("izquierda:", izquierda, "medio:", medio, "derecha:", derecha)
            input(enter)
            return izquierda, medio, derecha

        print("arreglo[index] < pivote:", arreglo[index] < pivote)
        print("arreglo[index] > pivote:", arreglo[index] > pivote)
        input(enter)
        if arreglo[index] < pivote:
            izquierda.append(arreglo[index])
            print("izquierda.append(arreglo[index]):", izquierda)
            input(enter)
        elif arreglo[index] > pivote:
            derecha.append(arreglo[index])
            print("derecha.append(arreglo[index]):", derecha)
            input(enter)
        else:
            medio.append(arreglo[index])
            print("medio.append(arreglo[index]):", medio)
            input(enter)

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
        input(enter)
        return particion(arreglo, pivote, izquierda, medio, derecha, index + 1)

    input(enter)
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
    input(enter)
    return quickSortPersonalizado(izquierda) + medio + quickSortPersonalizado(derecha)


arreglo = quickSortPersonalizado([3, 6, 8, 10, 1, 2, 1])
print(arreglo)