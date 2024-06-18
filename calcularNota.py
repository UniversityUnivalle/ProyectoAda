def calcularNota(n1, n2, n3, n4):
    
    n1 *= 0.2
    print(f"La nota uno calculada es: {n1}")
    n2 *= 0.3
    print(f"La nota dos calculada es: {n2}")
    n3 *= 0.2
    print(f"La nota tres calculada es: {n3}")
    n4 *= 0.3
    print(f"La nota cuatro calculada es: {n4}")
    
    print("-------------------")
    notaFinal = n1 + n2 + n3 + n4
    print(f"La nota final calculada es: {notaFinal}")

    
    return notaFinal


notaF = calcularNota(3.3, 2.9, 3.9, 2.2)

