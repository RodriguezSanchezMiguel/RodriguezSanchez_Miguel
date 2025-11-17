#Haz un programa que pida el nombre de un contacto y su teléfono, y los agregue a un diccionario.

nombre = input("Ingresa el nombre de tu contacto: ").lower()
numero = int(input("Ingresa el numero de tu contacto: "))

agenda = {}

agenda[nombre] = numero
print(agenda)

if len(str(numero)) < 10:
    print("El numero de telefono ingresado es invalido")
else:
    print("El contacto ha sido agregado correctamente")
