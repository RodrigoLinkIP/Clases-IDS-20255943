n = int(input())

pa, pb, pc = map(int, input().split(' '))

combos = []

for i in range(0 , n):
    combos.append(input())

for j in range(0, n):
    print(combos[j].count("A") * pa + combos[j].count("B") * pb + combos[j].count("C") * pc)