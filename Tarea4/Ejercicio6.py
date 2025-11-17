#Crea un diccionario con clave y valor producto : precio. Luego, pide una lista de productos comprados y muestra el total de la compra. Si el producto no existe, muestra una advertencia.

productos = {
    "manzana": 10,
    "leche": 25,
    "pan": 15,
    "huevo": 40,
    "arroz": 23,
    "aceite": 40,
    "queso": 33,
    "cereal": 50,
    "pollo": 95,
    "jugo": 12
}

productos_comprados = input("Ingresa los productos que compraste: ").lower().split()

total = 0

for producto in productos_comprados:
    if producto in productos:
        total += productos[producto]
    else:
        print(f"El producto '{producto}' no esta en el inventario")

print(f"El total de toda la compra es: ${total}")
