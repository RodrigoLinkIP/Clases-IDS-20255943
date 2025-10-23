a = int(input())
pers = []
cant = 0

for i in range(0, a):
    pers.append(int(input()))
    if pers[i] >= 15:
        cant = cant + 1

print(cant)