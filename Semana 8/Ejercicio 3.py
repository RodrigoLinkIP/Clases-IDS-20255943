# Sitema de gestión de alumnos

menu_iniciado = True
alumnos = []

while menu_iniciado:
    opcion = int(input("1. Agregar, 2. Consultar, 3. Modificar, 4. Borrar, 5. Salir: "))
    if opcion == 1:
        alumnos.append(input("Digite el nombre del alumno: "))
    elif opcion == 2:
        for a in alumnos:
            print(a)
    elif opcion == 3:
        alumnos[int(input("Digite el número del alumno (1-3): ")) - 1] = input("Digite el nombre nuevo: ")
    elif opcion == 4:
        alumno_borrado = alumnos.pop(int(input("Digite el número del alumno (1-3) a popear: ")) - 1)
        print(f"Hemos borrado a {alumno_borrado}")
    elif opcion == 5:
        menu_iniciado = False
    else:
        print("Esa opción no es valida")
        
        
print("Gracias por usar nuestro sistema")