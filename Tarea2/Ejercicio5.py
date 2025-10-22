#Haz un programa que pida un precio y muestre el total con IVA del 16%

precio = int(input("Ingresa el precio: "))
porcentaje = 16

resultado = (precio * (porcentaje /100))

preciofinal = (precio + resultado)

print(f'El precio total es: {preciofinal}')
