# Otro modula para comprender las funciones

# Definimos la funcion
def describir_mascota(nombre_mascota: str, tipo_animal: str = "perro"):
    """Esta funcion describe una mascota, por defecto tipo_animal = perro"""
    print(f"Mi mascota se llama {nombre_mascota.capitalize()}")
    print(f"y es un tipo de animal {tipo_animal.lower()}")
    
# Llamamos la funcion
# describir_mascota(nombre_mascota="phoenix", tipo_animal="perro")
# describir_mascota("misifus")

def registro_usuarios(nombre, apellido, inicial = "", edad = 0):
    """Construir un nombre a partir de sus componentes"""
    if edad:
        texto_completo = f"La persona {nombre} {inicial} {apellido}, de {edad} años de edad."
    else:
        texto_completo = f"La persona {nombre} {inicial} {apellido}"
    return texto_completo

# print(registro_usuarios("Daniel", "Wisecarver"))

# Definimos una funcion que es usa por una lista

def saludar_usuarios(nombres):
    """Saludará usuario"""
    for nombre in nombres:
        print(f"Hola, {nombre.capitalize()}")

usuarios = ["ana", "luis", "JUAN"]

saludar_usuarios(usuarios)