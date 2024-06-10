def eliminarUltimoLista(lista, index=0, nuevaLista=None):
    if nuevaLista is None:  
        nuevaLista = []

    if index == len(lista) - 1:
        lista[:] = nuevaLista
        return

    nuevaLista.append(lista[index])

    eliminarUltimoLista(lista, index + 1, nuevaLista)

lista = [1, 2, 3, 4]
eliminarUltimoLista(lista)
print(lista)  
