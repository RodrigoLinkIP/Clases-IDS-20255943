clientes = []
productos = []
pedidos = []
esen_brew = True

# zfill

while esen_brew:
    opcion = int(input("Ingrese el número de la acción que desee realizar: \n1) Mostrar productos \n2) Agregar producto \n3) Registrar nuevo cliente \n4) Mostrar clientes \n5) Registrar pedido \n6) Mostrar pedidos del día \n7) Mostrar categorias disponibles \n8) Salir Acción: \n"))
    print("")
    # Mostrar productos
    if opcion == 1:
        if len(productos) == 0:
            print("No hay productos ingresados")
        else:
            for product in productos:
               print(f"{product["nombre"]}: ${product["precio"]}")
        print("")
    # Agregar productos
    if opcion == 2:
        nuevo_producto = {
            "codigo": "P" + str(len(productos) + 1).zfill(3),
            "nombre": input("Ingrese el nombre del producto: "),
            "categoria": input("Ingrese la categoria del producto: "),
            "precio": float(input("Ingrese el precio del producto: ")),
        }
        productos.append(nuevo_producto)
        print("")
    # Registrar clientes
    if opcion == 3:
        nuevo_cliente = {
            "codigo": "C" + str(len(clientes) + 1).zfill(3),
            "nombre": input("Ingrese el nombre del cliente: "),
            "correo": input("Ingrese el correo del cliente: "),
            "telefono": input("Ingrese el número de telefono del cliente: ")
        }
        clientes.append(nuevo_cliente)
        print("")
    # Mostrar clientes
    if opcion == 4:
        if len(clientes) == 0:
            print("No hay clientes ingresados")
        else:
            for client in clientes:
               print(f"{client["nombre"]} \n  Correo: {client["correo"]}\n   Telefono: {client["telefono"]}")
        print("")
    # Registrar pedidos
    if opcion == 5:
        print("Estos son los clientes actuales: ")
        for cliente in clientes:
            print(f"{cliente["codigo"]}: {cliente["nombre"]}")
        print("")
        codigo_c = input("Ingrese el codigo del cliente: ")
        cant_productos = int(input("Ingrese la cantida de productos que desee ingresar: "))
        ped_productos = []
        print("Estos son los productos actuales: ")
        for producto in productos:
            print(f"{producto["codigo"]}: {producto["nombre"]}")
        for i in range(cant_productos):
            ped_productos.append(input("Ingrese el codigo del producto que desee ingresar: "))
        registrar_producto_nuevo = {
            "codigo_c": codigo_c,
            "codigos_p": ped_productos
        }
        pedidos.append(registrar_producto_nuevo)
        print("")
    # Mostrar pedidos del día
    if opcion == 6:
        if len(pedidos) == 0:
            print("No hay pedidos ingresados")
        else:
            for pedido in pedidos:
                total = 0
                print(f"El cliente {pedido["codigo_c"]} ha pedido estos productos: ")
                for codigo in pedido["codigos_p"]:
                    for products in productos:
                        if products["codigo"] == codigo:
                            print(f"    - {products["codigo"]}: {products["nombre"]} - ${products["precio"]}")
                            total += products["precio"]
                print(f"Pagará un total de ${total}")
        print("")
    # Mostrar categorias actuales
    if opcion == 7:
        categorias_rep = []
        if len(productos) == 0:
            print("No hay categorias ingresadas")
        else:
            for product in productos:
                categorias_rep.append(product["categoria"])
            categorias = set(categorias_rep)
            print("Estas son las cateogrias actuales: ")
            for categoria in categorias:
                print(categoria)
        print("")
    # Salir
    if opcion == 8:
        print("Saliendo del sistema")
        print("")
        esen_brew = False