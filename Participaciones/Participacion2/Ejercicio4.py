#Haz un programa que pida 5 números (Técnicamente podríamos almacenarlos en un arreglo, pero no hemos llegado ahí, así que NO LO HAGAS ASÍ, debes pedir los números y almacenarlos en variables diferentes), de los 5 números ingresados, muestra cuántos fueron mayores que 10

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))
num4 = int(input("Ingresa el cuarto numero: "))
num5 = int(input("Ingresa el quinto numero: "))

contador_mayores_10 = 0

if num1 > 10:
    contador_mayores_10 += 1 
if num2 > 10:
    contador_mayores_10 += 1
if num3 > 10:
    contador_mayores_10 += 1
if num4 > 10:
    contador_mayores_10 += 1
if num5 > 10:
    contador_mayores_10 += 1

print(f"De los 5 numeros ingresados, {contador_mayores_10} son mayores que 10")
