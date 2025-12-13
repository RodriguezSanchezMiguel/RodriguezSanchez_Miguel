#Haz un programa que pida al usuario ingresar un nombre y una edad, verifica si la persona ingresada tiene la edad suficiente para votar (Tomando en cuenta que se puede votar a partir de los 18 años), si puede votar imprime un mensaje indicando que se puede votar, en caso de que no se pueda, imprime un mensaje indicando que no se puede votar y los años que le faltan para llegar poder votar

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))


if edad >= 18:
    print(f"{nombre}, tienes {edad} años, tienes la edad suficiente para votar")
else:
    años_que_faltan = 18 - edad
    print(f"{nombre}, tienes {edad} años, no tienes la edad suficiente para votar, te faltan {años_que_faltan} años")
