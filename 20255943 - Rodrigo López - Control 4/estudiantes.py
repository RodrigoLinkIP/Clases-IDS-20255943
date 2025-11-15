def registrar_estudiante(estudiantes):
    # Se crea un diccionario con la información del nuevo estudiante
    nuevo_estudiante = {
        "codigo": "S" + str(len(estudiantes) + 1).zfill(3),
        "nombre": input("Ingrese el nombre del estudiante: ")
    }
    # Se guarda la variable nuevo_estudiante en la lista de estudiantes
    estudiantes.append(nuevo_estudiante)


def mostrar_estudiantes(estudiantes):
    # Se verifica que existan estudiantes apartir de la longitud de la lista
    if len(estudiantes) > 0:
        print("Estos son los libros disponibles: ")
        for valores in estudiantes:
            print("")
            print(f"Codigo: {valores["codigo"]} \nNombre: {valores["nombre"]}")
    else:
        print("Aun no se han ingresado estudiantes")