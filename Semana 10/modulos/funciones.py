# Este módulo contendrá las funciones

# Definiendo la función
def ordenar_pizza(size,masa,*ingredientes): # ahora con args
    """Vamos a imprimir su orden"""
    print(f"Usted ha ordenado una pizza {size} de masa {masa} de: ")
    for i in ingredientes:
        print(f"\t- {i.capitalize()}")

def registro_profesores(nombre, apellido, **materias):
    """Crear un registro de profesor, utilizando kwargs"""
    print(f"El profesor {nombre} {apellido} imparte las materias: ")
    for ciclo, materias in materias.items():
        print(f"\t - {ciclo}: \t{materias}")

def saludar_usuarios(nombres):
    """Saludará usuario"""
    for nombre in nombres:
        print(f"Hola, {nombre.capitalize()}")