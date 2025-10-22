#Haz un programa que pida un numero y muestre si esta entre 10 y 20

numero = int(input("Ingresa un numero: "))

resultado = (numero >= 10) and (numero <= 20)

print(f'¿Se cumple la proposicion? {resultado}')
