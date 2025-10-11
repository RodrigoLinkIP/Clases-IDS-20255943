e = int(input("Ingrese la cantidad de productos de enero: "))
f = int(input("Ingrese la cantidad de productos de febrero: "))
m = int(input("Ingrese la cantidad de productos de marzo: "))
costo_total = e * 1.25 + f * 1.38 + m * 1.14
print(f"El cosoto total de los articulos es de ${costo_total:.2f}")