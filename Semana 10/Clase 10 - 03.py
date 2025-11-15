# Vamos a proceder a atender pedidos de pizza

def ordenar_pizza(size,masa,*ingredientes): # ahora con args
    """Vamos a imprimir su orden"""
    print(f"Usted ha ordenado una pizza {size} de masa {masa} de: ")
    for i in ingredientes:
        print(f"\t- {i.capitalize()}")
    
# Llamando la funcion
ordenar_pizza("grande", "delgada", "queso", "jamon", "pepperoni", "chile", "tomate", "piña", "tocino")