from libros import registrar_libro, mostrar_libros
from estudiantes import registrar_estudiante, mostrar_estudiantes
from prestamos import registrar_prestamo, mostrar_prestamos

libros = []
estudiantes = []
prestamos = []

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar libro")
        print("2. Registrar estudiante")
        print("3. Registrar préstamo")
        print("4. Mostrar libros")
        print("5. Mostrar estudiantes")
        print("6. Mostrar préstamos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_libro(libros)
        elif opcion == "2":
            registrar_estudiante(estudiantes)
        elif opcion == "3":
            registrar_prestamo(libros, estudiantes, prestamos)
        elif opcion == "4":
            mostrar_libros(libros)
        elif opcion == "5":
            mostrar_estudiantes(estudiantes)
        elif opcion == "6":
            mostrar_prestamos(prestamos)
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

menu()
