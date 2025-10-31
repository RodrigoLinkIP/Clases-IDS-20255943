numeros = [1, 2, 3, 4]
# print(len(numeros))
palabra = "Aulas"
# print(len(palabra))
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

"""for x in dias:
    print(x[:2])"""
    
"""for numerito in range(0, 10, 2):
    print(numerito)
    
    
personas = ["Ana", "Luis", "Luisa"]

for p in personas:
    for l in p:
        print(l)"""
        
valores = [[1, 3, 6],
           [2, 7, 4],
           [6, 5, 9],
           [1, 10, 20]]
mayores = []
minimo = int(input("Digite el minimo: "))
for i in valores:
    for j in i:
        if j > minimo:
            mayores.append(j)

print(mayores)