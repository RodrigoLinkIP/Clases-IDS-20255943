aprobacion = True

while aprobacion:
    eleccion = input("Quieres seguir jugando? (Y/N) \n")
    if eleccion[0].upper() == "n":
        aprobacion = False
    elif eleccion[0].lower() == "y":
        print("Me alegra que quieras seguir jugando!")
    else:
        print("La opción elegida no es valida")