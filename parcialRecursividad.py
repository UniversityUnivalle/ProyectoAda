def algoritmoY(R, y, n):
    if y < n:
        R += y + 4
        return algoritmoY(R, y + 1, n)
    else:
        return R

def algoritmoZ(R, z, n):
    if z <= n:
        R += z * 5
        return algoritmoZ(R, z + 1, n)
    else:
        return R

def algoritmoGeneral(x, n, R):
    if x <= n:
        R = algoritmoY(R, 1, n)
        R = algoritmoZ(R, 0, n)
        return algoritmoGeneral(x + 1, n, R)
    else:
        return R

print(algoritmoGeneral(1, 2, 5))

print("Nuevo algoritmo divisores de 7")

# divisores_de_7.py

def divisores_de_7(arr):
    def helper(arr, index, result):
        if index == len(arr):
            return result

        if arr[index] % 7 == 0:
            result.append(arr[index])

        return helper(arr, index + 1, result)

    return helper(arr, 0, [])

# Ejemplo de uso
lista = [14, 23, 35, 50, 49, 7, 21, 100]
print(divisores_de_7(lista))


