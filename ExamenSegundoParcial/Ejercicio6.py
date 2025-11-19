#Pide al usuario ingresar 10 productos y almacenarlos en una lista luego muestra la lista ordenada alfabeticamente

productos = []

for i in range(10):
    producto = input("Ingresa el nombre del producto: ")
    productos.append(producto)

productos.sort()
print("La lista de los productos ordenados alfabeticamente son:" , productos)