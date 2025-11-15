def registrar_libro(libros):
    # Se crea un diccionario con la información del nuevo libro
    nuevo_libro = {
        "codigo": "L" + str(len(libros) + 1).zfill(3),
        "titulo": input("Ingrese el titulo del libro: "),
        "autor": input("Ingrese el autor del libro: "),
        "disponible": True
    }
    # Se guarda la variable nuevo_libro en la lista de libros
    libros.append(nuevo_libro)



def mostrar_libros(libros):
    # Se verifica que existan libros apartir de la longitud de la lista
    if len(libros) > 0:
        print("Estos son los libros disponibles: ")
        # Los imprime por medio de un for
        for valores in libros:
            print("")
            print(f"Codigo: {valores["codigo"]} \nTitulo: {valores["titulo"]} \nAutor: {valores["autor"]} \nEstado: {"Disponible" if valores["disponible"] == True else "Ocupado"}")
    else:
        print("Todavia no se han ingresado libros")