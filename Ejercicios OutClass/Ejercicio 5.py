# https://omegaup.com/arena/problem/Blancas-Vs-Negras

m, n = map(int, input().split(' '))
piezas = []
b = 0
n = 0
rb = 0
rn = 0

for i in range(m):
    piezas.append(list(map(int, input().split(' '))))
    
k, l = map(int, input().split(' '))

for i in piezas:
    for e in i:
        if e % 2 == 0:
            n += 1
        else:
            b += 1
    rb = i.count(l)
    rn = i.count(k)

print(f"{n} {b}")
if rb == 1 and rn == 0 or rb == 0 and rn == 1:
    print("JAQUE MATE")
else:
    print("NO JAQUE")