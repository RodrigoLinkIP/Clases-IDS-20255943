# Variables de validación
cafeteria = True
admin = False
encargado = False
estudiante = False

# Precio base becados 2.75

# Listas de guardados, usuario admin predefinido
usuarios = [
    {
        "codigo": "00002222",
        "nombre": "Mario",
        "rol": "admin",
        "becado": "no",
        "contraseña": "1234"
    }
]
platos = []
complementos = []
pedidos = []

# Menu inicial

while cafeteria:
    # A partir de tu codigo y tu rol, ingresaras al menu que te corresponda
    
    codigo = input(f"Ingrese su codigo: ")
        
    for usuario in usuarios:
        if usuario["codigo"] == codigo:
            if usuario["rol"] == "admin":
                if input("Ingrese su contraseña: ") == usuario["contraseña"]:
                    admin = True
                else:
                    print("Contraseña incorrecta")
            elif usuario["rol"] == "encargado":
                encargado = True
            elif usuario["rol"] == "estudiante":
                estudiante = True
            break
    else:
        print("El usuario no fue encontrado")
        
    while admin == True:
        while True:
            try:
                opcion = int(input("Ingrese el número de la acción que desee realizar: \n1) Agregar usuario \n2) Mostrar usuarios \n3) Modificar usuario \n4) Eliminar usuario \n5) Salir \n"))
                print("")
                # Agregar usuario
                if opcion == 1:
                    en_es = input("¿Desea agregar un encargado o un estudiante? ").lower()
                    if en_es == "encargado":
                        nuevo_usuario = {
                            "codigo": input("Ingrese el codigo del encargado: "),
                            "nombre": input("Ingrese el nombre del encargado: "),
                            "rol": en_es,
                            "becado": "no",
                            "contraseña": input("Ingrese la contraseña del encargado")
                        }
                        usuarios.append(nuevo_usuario)
                    elif en_es == "estudiante":
                        nuevo_usuario = {
                            "codigo": input("Ingrese el codigo del estudiante: "),
                            "nombre": input("Ingrese el nombre del estudiante: "),
                            "rol": en_es,
                            "becado": input("¿Está becado el estudiante (Si/No)? ").lower()
                        }
                        usuarios.append(nuevo_usuario)
                    else:
                        print("No está permitido ese valor")
                    print("")
                if opcion == 2:
                    print("-" * 71)
                    print(f"|{" Codigo ".center(15, "-")} | {" Nombre ".center(15, "-")} | {" Rol ".center(15, "-")} | {" Becado ".center(15, "-")}|")
                    print("-" * 71)
                    for usuario in usuarios:
                        if usuario["rol"]:
                            print(f"|{usuario["codigo"].center(15, " ")} | {usuario["nombre"].center(15, " ")} | {usuario["rol"].capitalize().center(15, " ")} | {usuario["becado"].capitalize().center(15, " ")}|")
                    print("")
                if opcion == 3:
                    codigo = input("Ingrese el codigo del usuario que desee modificar: ")
                    for usuario in usuarios:
                        if usuario["codigo"] == codigo and usuario["rol"] != "admin":
                            for key, value in usuario.items():
                                print(f"Ingrese el nuevo valor de {key}, sino dejar en blanco")
                                usuario[key] = value if (x := input()) == "" else x
                    print("")
                if opcion == 4:
                    codigo = input("Ingrese el codigo del usuario que desea eliminar: ")
                    print("")
                    for usuario in usuarios:
                        if usuario["codigo"] == codigo and usuario["rol"] != "admin":
                            print("Este es el usuario que eliminará")
                            print("-" * 71)
                            print(f"|{" Codigo ".center(15, "-")} | {" Nombre ".center(15, "-")} | {" Rol ".center(15, "-")} | {" Becado ".center(15, "-")}|")
                            print("-" * 71)
                            print(f"|{usuario["codigo"].center(15, " ")} | {usuario["nombre"].center(15, " ")} | {usuario["rol"].capitalize().center(15, " ")} | {usuario["becado"].capitalize().center(15, " ")}|")
                            if input("Desea proseguir (Si-No)? ").lower() == "si":
                                usuario_eliminado = usuarios.pop(usuarios.index(usuario))
                            else:
                                print("Eliminación cancelada!")
                        else:
                            print("El codigo es invalido o no existe")
                    print("")
                if opcion == 5:
                    admin = False
            except ValueError:
                print("Valor ingresado no permitido")
    
    while encargado == True:
        while True:
            try:
                opcion = int(input("Ingrese el número de la acción que desee realizar: \n1) Agregar platos \n2) Visualizar Menú \n3) Limpiar Menú \n"))
                print("")
                # Agregar platos
                if opcion == 1:
                    nuevo_plato = {
                        "nombre": input("Ingrese el nombre del plato: ").lower(),
                        "precio": float(input("Ingrese el precio del plato: ")),
                        "cantidad": int(input("Ingrese la cantidad disponible del plato: ")),
                    }
                    platos.append(nuevo_plato)
                    print("")
                if opcion == 2:
                    if len(platos) == 0:
                        print("Aun no se han ingresado platos")
                    else:
                        for plato in platos:
                            print(f"{plato["nombre"].capitalize()} \n   Precio: ${plato["precio"]} \n   Disponibles: {plato["cantidad"]}")
                    print("")
                if opcion == 3:
                    if len(platos) == 0:
                        print("Aun no se han ingresado platos")
                    else:
                        for plato in platos:
                            print(f"{plato["nombre"].capitalize()} \n   Precio: ${plato["precio"]} \n   Disponibles: {plato["cantidad"]}")
                    print("")
                # Salir vista encargado
                if opcion == 4:
                    encargado = False
                    break
            except ValueError:
                print("Entrada invalida, por favor ingrese un valor entero")
    
    while estudiante == True:
        while True:
            try:
                codigo = input("Ingrese su codigo de carnet: ")
                opcion = int(input("Ingrese el número de la acción que desee realizar: \n1) Visualizar Menú \n"))
                if opcion == 1:
                    if len(platos) == 0:
                        print("Todavía no hay platos disponibles")
                    else:
                        print("Este es el menú del día")
                        for plato in platos:
                            if plato["cantidad"] > 0:
                                print(f"- {plato["nombre"]}: ${[plato["precio"]]}")
                        print("Estos son los complementos disponibles")
                if opcion == 4:
                    estudiante = False
                    break
            except ValueError:
                print("Entrada invalida, por favor ingrese un valor entero")
