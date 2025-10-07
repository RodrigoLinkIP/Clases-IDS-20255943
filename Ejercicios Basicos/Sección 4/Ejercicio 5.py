product = input("Ingrese un producto: ")
price = float(input("Ingrese el precio del producto: "))
quantity = int(input("Ingrese la cantidad que desea comprar: "))
total = price * quantity

print(f"\nProducto: {product} \nPrecio: {price} \nCantidad: {quantity} \nTotal a pagar: ${total:.2f}")