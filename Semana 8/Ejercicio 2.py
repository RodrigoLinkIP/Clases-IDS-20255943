# Una aplicación para registrar alumnos

alumnos = []

"""
alumno = input("Digite el nombre: ")
alumnos.append(alumno)
alumno = input("Digite el nombre: ")
alumnos.append(alumno)
alumno = input("Digite el nombre: ")
alumnos.append(alumno)
"""

for a in range(int(input("Digite la cantidad de alumnos a registrar: "))):
    alumnos.append(input("Digite el nombre: "))

print(alumnos)