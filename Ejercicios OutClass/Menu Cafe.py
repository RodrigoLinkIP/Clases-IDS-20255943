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
reservas = []

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
                if input("Ingrese su contraseña: ") == usuario["contraseña"]:
                    encargado = True
                else:
                    print("Contraseña incorrecta")
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
                            "contraseña": input("Ingrese la contraseña del encargado: ")
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
                    break
            except ValueError:
                print("Valor ingresado no permitido")
    
    while encargado == True:
        while True:
            try:
                opcion = int(input("Ingrese el número de la acción que desee realizar: \n1) Agregar platos \n2) Agregar complementos \n3) Visualizar platos \n4) Visualizar complementos \n5) Visualizar Reservas \n6) Limpiar Menú y Reservas \n7) Salir \n"))
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
                    nuevo_complemento = {
                        "nombre": input("Ingrese el nombre del complemento: ").lower(),
                        "cantidad": int(input("Ingrese la cantidad disponible del complemento: ")),
                    }
                    complementos.append(nuevo_complemento)
                    print("")
                if opcion == 3:
                    if len(platos) == 0:
                        print("Aun no se han ingresado platos")
                    else:
                        for plato in platos:
                            print(f"{plato["nombre"].capitalize()} \n   Precio: ${plato["precio"]} \n   Disponibles: {plato["cantidad"]}")
                    print("")
                if opcion == 4:
                    if len(complementos) == 0:
                        print("Aun no se han ingresado complementos")
                    else:
                        for complemento in complementos:
                            print(f"{complemento["nombre"].capitalize()} \n   Disponibles: {complemento["cantidad"]}")
                    print("")
                if opcion == 5:
                    if len(reservas) == 0:
                        print("Aun no hay reservas realizadas")
                    else:
                        print("Estas son las reservas realizadas:")
                        print("-" * 114)
                        print(f"|{" Carnet ".center(20, "-")} | {" Plato ".center(20, "-")} | {" Complementos ".center(20, "-")} | {" Tortilla ".center(20, "-")} | {" A pagar ".center(20, "-")}|")
                        print("-" * 114)
                        for reserva in reservas:
                            print(f"|{reserva["codigo_estudiante"].center(20, " ")} | {reserva["plato"].capitalize().center(20, " ")} | {(reserva["complemento1"].capitalize() + ', ' + reserva["complemento2"].capitalize()).center(20, " ")} | {reserva["tortilla"].capitalize().center(20, " ")} | {str(reserva["precio"]).center(20, " ")}|")
                    print()
                if opcion == 6:
                    print("¿Está seguro que desea limpiar el menú? Esto eliminará todos los platos y complementos")
                    if input("Ingrese Si para confirmar: ").lower() == "si":
                        platos.clear()
                        complementos.clear()
                        reservas.clear()
                        print("Menú y reservas limpiados exitosamente")
                    else:
                        print("Limpieza cancelada")
                    print("")
                # Salir vista encargado
                if opcion == 7:
                    encargado = False
                    break
            except ValueError:
                print("Entrada invalida, por favor ingrese un valor entero")
    
    while estudiante == True:
        while True:
            try:
                codigo = input("Ingrese su codigo de carnet: ")
                opcion = int(input("Ingrese el número de la acción que desee realizar: \n1) Visualizar Menú \n2) Salir \n"))
                print("")
                if opcion == 1:
                    if len(platos) == 0:
                        print("Todavía no hay platos disponibles")
                    else:
                        print("Estos son los platos disponibles: ")
                        for i, plato in enumerate(platos, start=1):
                            print(f"{i}- {plato["nombre"].capitalize()}: ${plato["precio"]}")
                        print("Estos son los complementos disponibles: ")
                        for i, complemento in enumerate(complementos, start=1):
                            print(f"{i}- {complemento["nombre"].capitalize()}: Disponibles: {complemento["cantidad"]}")
                        print("")
                        if input("Si desea reservar un plato, ingrese Si: ").lower() == "si":
                            plato_elegido = False if (x := int(input("Ingrese el número del plato que desea reservar: "))) > len(platos) or x <= 0 else x - 1
                            complemento1_elegido = False if (y := int(input("Ingrese el número del primer complemento que desea reservar: "))) > len(complementos) or y <= 0 else y - 1
                            complemento2_elegido = False if (z := int(input("Ingrese el número del segundo complemento que desea reservar: "))) > len(complementos) or z <= 0 else z - 1
                            if plato_elegido is not False:
                                if platos[plato_elegido]["cantidad"] > 0 and complementos[complemento1_elegido]["cantidad"] > 0 and complementos[complemento2_elegido]["cantidad"] > 0:
                                    nueva_reserva = {
                                        "codigo_estudiante": codigo,
                                        "plato": platos[plato_elegido]["nombre"],
                                        "complemento1": "ninguno" if complemento1_elegido is False else complementos[complemento1_elegido]["nombre"],
                                        "complemento2": "ninguno" if complemento2_elegido is False else complementos[complemento2_elegido]["nombre"],
                                        "tortilla": "si" if input("¿Desea agregar tortilla (Si/No)? ").lower() == "si" else "no",
                                        "precio": platos[plato_elegido]["precio"] - 2.75 if usuario["becado"].lower() == "si" else platos[plato_elegido]["precio"]
                                    }
                                    reservas.append(nueva_reserva)
                                    platos[plato_elegido]["cantidad"] -= 1
                                    complementos[complemento1_elegido]["cantidad"] -= 1
                                    complementos[complemento2_elegido]["cantidad"] -= 1
                                    print("Reserva realizada con éxito")
                                else:
                                    print("El plato o los complementos seleccionados no están disponibles")
                            else:
                                print("El plato seleccionado no es válido")
                if opcion == 2:
                    estudiante = False
                    break
            except ValueError:
                print("Entrada invalida, por favor ingrese un valor entero")
