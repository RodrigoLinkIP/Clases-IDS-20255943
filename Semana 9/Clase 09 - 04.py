# Enumerate
usuarios = ["Ana", "Carlos", "Luis", "Maria", "Lorenzo"]
edades = [20, 19, 21, 22, 18]
frutas = ["Mango", "Fresa", "Pera", "Sandia", "Piña"]

"""for posicion, usuario in enumerate(usuarios, start=1):
    print(f"{posicion} {usuario}")"""
for usuario, edad, fruta in zip(usuarios, edades, frutas):
    print(f"El usuario {usuario}, con edad {edad}, le gusta {fruta}")