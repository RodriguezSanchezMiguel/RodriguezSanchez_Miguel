# Ejercicio 3: Haz un programa en Python que pida un numero entero y muestre cuantos numeros pares hay desde el 1 hasta ese numero (incluyendo si es par)

conteo_pares = 0
#Solicitar al usuario qur ingrese un numero
numero = int(input("Ingresa un numero entero: "))

for i in range(1, numero + 1):

    if i % 2 == 0:
        conteo_pares += 1
    print(i)

print(f"Hay {conteo_pares} numeros pares desde 1 hasta {numero}")

print("----------------------------------------")

#Ejercicio 4: Haz un programa en Python que pida un numero y calcule el factorial de ese numero utilizado un ciclo for.

numero = int(input("Ingresa un numero para calcular su factorial: ")) 
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print(f"El factorial de {numero} es {factorial}")

print("----------------------------------------")

#Bucle While
#While condicion:
#   bloque de codigo

#Ejercicio 1: Haz un programa que pida al usuario ingresar una contraseña hasta que ingrese la correcta, y que tenga maximo de 5 intentos.

contraseña_correcta = "Credinalga"
intentos = 0
max_intentos = 5
contraseña = input("Ingresa la contraseña: ")

while (intentos < max_intentos) and (contraseña != contraseña_correcta):
    print("Contraseña incorrecta. Intenta de nuevo.")
    intentos += 1
    contraseña = input("Ingresa la contraseña: ")

if intentos == max_intentos:
    print("Has excedido el número máximo de intentos. Acceso denegado.")
else:
    print(f"Contraseña correcta. Acceso concedido. Intentos realizados {intentos}.")
        
    print("----------------------------------------")

    #Ejercicio 2: Haz un programa que pida al usuario ingresar numeros positivos y que se detenga hasta que ingrese un numero negativo.

    numero = float(input("Ingresa un numero positivo (o un numero negativo para salir)"))

    while numero >= 0:
        numero = float(input("Ingresa un numero positivo (o un numero negativo para salir)"))

    print("Has ingresado un numero negativo. Programa ha terminado.")

    print("----------------------------------------")

#Ejercicio 3: Haz un programa que sume todos los numeros que ingrese el usuario hasta que ingrese un 0.

suma = 0
numero = float(input("Ingresa un numero para sumar (o 0 para salir): "))

while numero != 0:
    suma += numero
    numero = float(input("Ingresa un numero para sumar (o 0 para salir): "))
print(f"La suma total de los numeros ingresados es: {suma}")
