#Haz un programa que pida un numero entero N y calcula la suma de todos los numeros del 1 al N

numero = int(input("Ingresa un numero entero: "))
suma = 0

for i in range(1, numero +1):
    suma += i

print("La suma de todos los numeros del hasta ", numero, "es:", suma)
