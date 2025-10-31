# https://omegaup.com/arena/problem/Yael-no-quiere-reprobar/#problems

h = int(input())
nums = list(map(int, input().split(' ')))
cant = 0
for i in range(0, len(nums)):
    if h == nums[i]:
        cant = 1
        break
    if h > nums[i]:
        cant += 1
        h -= nums[i]

if cant == 0:
    print("Yael reprueba el semestre, aprendan de Yael y hagan sus tareas")
if cant == 1:
    print("Yael aprueba al menos una de las 3 materias que le faltaban")
if cant == 3:
    print("Yael aprueba todas sus materias")


