"""nota = float(input("Indique la nota: "))

if nota >= 6:
    print("Pasó")
else:
    print("No pasó")"""


# nota = int(input("Ingrese la nota: "))

"""if nota == 10:
    print("Excelente")
elif nota > 7:
    print("Muy bien")
elif nota > 5:
    print("Bien")
elif nota > 3:
    print("Regular")
else:
    print("Mal")"""


"""if nota == 10:
    print("Excelente")
else:
    if nota > 7:
        print("Muy bien")
    else:
        if nota > 5:
            print("Bien")
        else:
            if nota > 3:
                print("Regular")
            else:
                print("Mal")"""


monto = int(input("Ingrese el monto: "))
tipo_impuesto = input("Ingrese el tipo de impuesto (Local-Export): ")
impuesto = 0

if tipo_impuesto.lower() == "local":
    if monto > 500:
        impuesto = 0.1
    elif monto > 200:
        impuesto = 0.08
    elif monto > 50:
        impuesto = 0.06
    else:
        impuesto = 0
elif tipo_impuesto.lower() == "export":
    if monto > 500:
        impuesto = 0.14
    elif monto > 200:
        impuesto = 0.12
    elif monto > 50:
        impuesto = 0.1
    else:
        impuesto = 0
else:
    print("Valor no valido")
    