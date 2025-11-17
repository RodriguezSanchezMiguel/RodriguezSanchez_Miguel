#Haz un programa que pida 5 nombres y luego pregunte uno; si está en la lista, muestra “Encontrado”.

nombres = []
for i in range(5):
    nombre = input("Ingresa tu nombre: ")
    nombres.append(nombre.lower())

buscar = input("ingresa tu nombre para buscarlo: ").lower()
if buscar in nombres:
    print("Tu nombre si esta en la lista")
else:
    print("Tu nombre no ha sido ingresado en la lista. Busca otro nombre que haya sido ingresado.")
