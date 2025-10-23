"""lista = [1, 2, "tres", ["ene", "feb", "mar"]]

print(len(lista))
print(lista)

# Agarra el tercer elemento del tercer elemento de la lista xd
print(lista[2][2].upper())

# Agarra el segundo elemento del tercer elemento del caurto elemento de la lista XDDD
print(lista[3][2][1].upper())"""

# 4 colecciones, 1 la lista, las otras tres los strings
numeros = ["uno", "dos", "tres"]
numero = numeros + ["cuatro", "cinco", "seis"]

print(numero)

numero[2] = "three"
print(numero)