def quickSortPersonalizado(arreglo):
    if len(arreglo) <= 1:
        return arreglo

    pivote = arreglo[0]
    izquierda = []
    medio = []
    derecha = []

    def particion(arreglo, pivote, izquierda, medio, derecha, i=0):
        if i == len(arreglo):
            return izquierda, medio, derecha

        if arreglo[i] < pivote:
            izquierda.append(arreglo[i])
        elif arreglo[i] > pivote:
            derecha.append(arreglo[i])
        else:
            medio.append(arreglo[i])

        return particion(arreglo, pivote, izquierda, medio, derecha, i + 1)

    izquierda, medio, derecha = particion(arreglo, pivote, izquierda, medio, derecha)

    return quickSortPersonalizado(izquierda) + medio + quickSortPersonalizado(derecha)