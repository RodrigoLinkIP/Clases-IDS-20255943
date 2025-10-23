sls = []
n = int(input())

for i in range (0, n):
    sls.append(int(input()))

for j in range(0, n):
    if sls[j] >= 3:
        print("Ok")
    else:
        print("No")