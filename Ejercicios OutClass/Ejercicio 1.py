# https://omegaup.com/arena/problem/ofmi-2023-bruja/#problems

n = int(input())

result = list(map(int, input().split(' ')))
suma = 0
for j in range(0, len(result) - 1):
    for i in range(j, len(result) - 1):
        suma += (result[j] * result[i + 1])
print(suma)

