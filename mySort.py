def quickSortPersonalizado(arreglo):
    if len(arreglo) <= 1:
        return arreglo

    pivote = arreglo[0]
    izquierda = []
    medio = []
    derecha = []

    def particion(arreglo, pivote, izquierda, medio, derecha, index=0):
        if index == len(arreglo):
            return izquierda, medio, derecha
        
        if arreglo[index] < pivote:
            izquierda.append(arreglo[index])
        elif arreglo[index] > pivote:
            derecha.append(arreglo[index])
        else:
            medio.append(arreglo[index])

        return particion(arreglo, pivote, izquierda, medio, derecha, index + 1)

    izquierda, medio, derecha = particion(arreglo, pivote, izquierda, medio, derecha)

    return quickSortPersonalizado(izquierda) + medio + quickSortPersonalizado(derecha)