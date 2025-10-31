# Aplicación para una cafetería de gestión de platos y pedidos #
# Las partes estan separadas por comentarios de numerales y los resultados descritos por comentarios de triple comilla

# 1. Configuración inicial

agente = "Encargado"
platillo = []
precios = []

"""
Se declaran 3 variables: un string y dos listas """

# 2. Ingreso a la aplicación

validacion = False

while validacion != True:
    if input("Favor ingrese el nombre del agente: ").lower() == agente.lower():
        validacion = True
    else:
        print("Agente no registrado")

"""
Mediante un bucle while con un condicional llamado validación, se confirma
si el nombre del agente es Encargado, medicante la comparación de ambos en formato lower()"""     

# 3. Gestión del menú principal

menu_principal = True

while menu_principal:
    eleccion = int(input("Elija una de las opciones de menú \n1. Creación de platillos 2. Consulta de platillos y precios 3. Colocar un pedido 4. Salir: "))
    print(" ")
    
    """
    Mediante un bucle while con un condicional llamado menu_princial, se iniciará la aplicación
    hasta que se elija lo contrario
    Se declara una variable llamada elección que es igual al input
    ingresado de cualquiera número de las opciones disponibles"""
    
    
    # 4. Creación de platillos
    
    if eleccion == 1:
        platillo.append(input("Ingrese el nombre del platillo a crear: ").lower())
        precios.append(float(input("Ingrese el precio del platillo a crear: ")))
        print(" ")
        
        """
        El usuario ingresó la opción 1, por ende podrá crear un platillo y asignarle un precio
        El nombre del platillo ingresado será guardado en minusculas
        El precio del platillo aceptará decimales"""
        
        # 5. Consulta de platillos y precios
        
    elif eleccion == 2:
        if len(platillo) == 0:
            print("Actualmente no hay platillos ingresados")
        else:
            for i in range(len(platillo)):
                print(f"{platillo[i].capitalize()}: ${precios[i]:.2f}")
        print(" ")
        
        """
        El usuario ingresó la opción 2, dicha opción le mostrará los platillos disponibles
        en caso de que no, mostrará un mensaje
        Mediante un bucle for obtendremos el platillo y el precio ya que ambos estan conectados
        por el mismo indice
        Debido a que los platillos son guardados en minuscula, usaremos la funcion capitalize()
        para convertir la primera letra en mayuscula
        De igual forma, el precio se mostrará con dos decimales"""
        
        
        # 6. Colocar un pedido
        
    elif eleccion == 3:
        platillo_elegir = input("Indique el nombre del platillo para su orden: ").lower()
        if platillo.count(platillo_elegir) > 0:
            indice = platillo.index(platillo_elegir)
            print(f"Usted a elegido {platillo[indice].capitalize()} con un precio de ${precios[indice]:.2f}")
            print(" ")
        else:
            print("El nombre del platillo no existe")
            print(" ")
            
            """
            El usuario ingresó la opción 3, en esta se colocará un pedido
            Con una variable llamada platillo_elegir se ingresará el nombre del platillo
            este será guardado en minusculas
            Con una validación se verificará si exise el platillo ingresado en platillos, mediante un count()
            Si sí existe, se tomará el indice del platillo y es el que se usará para tomar el propio platillo
            y su precio
            Si no existe, se mostrará un mensaje y volverá al menú"""
            
            # 7. Salir
            
    elif eleccion == 4:
        menu_principal = False
        
        """
        El usuario ingresó la opción 4, saldrá del mensaje
        Le da el valor de False a menu_principal, variable utilizada para mantener el bucle while activo"""
        
    else:
        
        """
        En caso de que la opción ingresada no exista, mostrará un mensaje y volverá al menú"""
        
        print("Esa opción no es valida")
        print(" ")