"""nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
numslt = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")"""

dui = input()
large = len(dui) == 10
ncharacter = dui[8] == "-"
ulti = dui[-1].isdigit()
# ulti = nums.count(dui[-1]) == 1 or numslt.count(dui[-1]) == 1

"""
Verficando si el dui ingresado tiene:
    - Al menos 10 caracteres
    - El caracter 9 es '-'
    - El último caracter es un número entero
"""

print(large and ncharacter and ulti)