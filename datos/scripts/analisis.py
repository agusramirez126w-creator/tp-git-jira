ventas = [100, 200, 300, 150]

total = sum(ventas)
promedio = total / len(ventas)
maximo = max(ventas)

print("Ventas totales:", total)
print("Promedio:", promedio)
print("Venta máxima:", maximo)

archivo = open("../resultados/resultados.txt", "w")

archivo.write(f"Ventas totales: {total}\n")
archivo.write(f"Promedio: {promedio}\n")
archivo.write(f"Venta máxima: {maximo}")

archivo.close()
