n = int(input())

pa, pb, pc = map(int, input().split(' '))

combos = []

for i in range(0 , n):
    combos.append(input())
    print(combos[i].count("A") * pa + combos[i].count("B") * pb + combos[i].count("C") * pc)