#Pide una cantidad de productos y su precio uno por uno, luego muestra el total con IVA del 16%

productos = int(input("Ingresa la cantidad de productos: "))
producto_sin_iva = 0 

for i in range(1, productos + 1):
    precio = float(input(f"Ingresa el precio del producto {i}: "))
    producto_sin_iva += precio

iva = producto_sin_iva * 0.16
producto_con_iva = producto_sin_iva + iva  

print(f"Total con IVA: ${producto_con_iva:}")
