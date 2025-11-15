def registrar_prestamo(libros, estudiantes, prestamos):
    # Se pide el carnet del estudiante
    carnet_estudiante = input("Ingrese el codigo del estudiante: ").capitalize()
    # Se verifica con existe_estudiante si el estudiante existe
    existe_estudiante = True if carnet_estudiante in (e["codigo"] for e in estudiantes) else False
    if not existe_estudiante: 
        print("El codigo no existe")
    else:
        # Se pide el codigo del libro
        codigo_libro = input("Ingrese el codigo del libro: ").capitalize()
        # Se verifica con existe_libro si el libro existe
        existe_libro = True if codigo_libro in (e["codigo"] for e in libros) else False
        if not existe_libro:
            print("El codigo no existe")
        else:
            for libro in libros:
                # Con un for y un if se verifica si el libro tiene el mismo codigo que el ingresado y si está disponible
                if libro["codigo"] == codigo_libro and libro["disponible"] == True:
                    nuevo_prestamo = {
                        "codigo_estudiante": carnet_estudiante,
                        "codigo_libro": codigo_libro,
                        "fecha": input("Ingrese la fecha del prestamo: "),
                    }
                    # Se agruega nuevo_prestamo a la lista de prestamos
                    prestamos.append(nuevo_prestamo)
                    # Con el for se busca y se le da el valor de False, para que esté ocupado cuando encuentre el libro con el codigo ingresado sino se mantiene normal
                    for libro in libros:
                        libro["disponible"] = False if libro["codigo"] == codigo_libro else libro["disponible"]
                elif libro["codigo"] == codigo_libro and libro["disponible"] == False:
                    print("El libro no está disponible")
                    
# Más facil de explicar esto en persona             
                

def mostrar_prestamos(prestamos):
    # Se verifica que existan prestamos apartir de la longitud de la lista
    if len(prestamos) > 0:
        for valores in prestamos:
            print("")
            print(f"Carnet del estudiante: {valores["codigo_estudiante"]} \nCodigo del libro: {valores["codigo_libro"]} \nFecha de prestamo: {valores["fecha"]}")
    else:
        print("Aun no se han ingresado prestamos")