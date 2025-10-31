# https://omegaup.com/arena/problem/ofmi-2023-bruja/#problems

n = int(input())

result = list(map(int, input().split(' ')))
final = []
for i in range(0, len(result)):
    if i > result.index(result[-1]) and i >= len(result):
        break
    if result.count(result[i]) != 1:
        result.pop(i)
print(len(result))

