#Haz un programa que pida el radio y la altura de un cilindro y muestre su volumen
import math

radio = int(input("Ingresa el radio del cilindro: "))
altura = int(input("Ingresa la altura del cilindro: "))

volumen = (math.pi * radio ** 2 * altura)

print(f'El volumen del cilindro es: {volumen}')
