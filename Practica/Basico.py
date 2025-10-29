#Saludo personalizado, pide al usuario nombre y edad y muestra un saludo

Nombre = input("Igresa tu nombre: ")
Edad = int(input("Ingresa tu edad: "))

print(f'Hola {Nombre}, tienes {Edad} años. ')

print("---------------------------------")

#Operaciones matematicas, pide dos numeros al usuario y muestra la suma, resta, multiplicacion y la division

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

suma = (num1 + num2)
resta = (num1 - num2)
multiplicacion = (num1 * num2)
division = (num1 / num2)

print(f'La suma es {suma}, la resta es {resta}, la multiplicacion es {multiplicacion} y la division es {division}')

print("------------------------------")

#Numero par o impar, pide un numero y determina si es par o impar

numero = int(input("Ingresa un numero: "))

if numero % 2 ==0:
    print(f"El numero {numero} es par")
else:
    print(f"el numero {numero} es impar")

    print("-------------------------------")

    #Mayor de tres numeros, pide al usuario tres numeros y muestra cual es mayor

    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    num3 = int(input("Ingresa el tercer numero: "))

numero_mayor = max(num1, num2, num3)
 
print(f"El numero mayor es {numero_mayor}")

print("-------------------------")

#Tabla de multiplicar, pide un numero y muestra su tabla de multiplicar del 1 al 10

numero = int(input("Ingresa un numero: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i 
    print(f'{numero} x {i} = {resultado}')

    print("--------------------------")
