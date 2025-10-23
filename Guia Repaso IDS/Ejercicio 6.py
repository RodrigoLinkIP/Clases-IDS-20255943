nombres = []
n = int(input())

for i in range (0, n):
    nombres.append(input())

for j in range(0, n):
    if len(nombres[j]) >= 8:
        print("Si aguanto otro desarrollo de personaje")
    if len(nombres[j]) <= 6:
        print("No vale la pena")
    if len(nombres[j]) > 6 and len(nombres[j]) < 8:
        print("Dios no creo aguantar esta vez")