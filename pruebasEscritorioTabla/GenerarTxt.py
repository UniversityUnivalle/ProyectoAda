def GenerarText(tabla, arreglo, nombreArchivo, resultado):
    with open(f"{nombreArchivo}.txt", "w") as file:
        file.write(f"Arreglo: {arreglo} \n")
        file.write(f"{tabla}\n")
        file.write(f"Resultado: {resultado}")