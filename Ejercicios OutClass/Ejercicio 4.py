# https://omegaup.com/arena/problem/La-loca-hora-del-te/#problems

m, n = map(int, input().split(' '))
animl = [input() for _ in range(n)]

indx = []
asie = []
offset = 0

for i in range(1, len(animl) + 1):
    asie.append(i)

for i in range(int(input())):
    accs = input().split()
    if accs[0] == "T":
        offset += 1
    else:
        asie_ini = animl.index(accs[1]) + 1
        asie_act = ((asie_ini + offset - 1) % m) + 1
        indx.append(asie_act)

for i in indx:
    print(i)
