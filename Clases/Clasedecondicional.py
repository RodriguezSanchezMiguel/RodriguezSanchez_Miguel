#Ejercicio 1: Programa que pida un numero y muestre si es positivo, negativo o cero,
numero = float(input("Ingrese un numero: "))


if numero > 0:
    print("Bloque if ejecutado.")
    print("El numero es positivo. ")
elif numero < 0:
    print("Bloque elif ejecutado.")
    print("El numero es negativo. ")
else:
    print("Bloque else ejecutado.")
    print("El numero es cero. ")

print("----------------------")

#Ejercicio 2: Programa que pida dos numeros y muestre cual es mayor o si son iguales

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero numero: "))

if num1 > num2:
    print("El primer numero es el mayor.")
elif num1 < num2:
    print("El segundo numero es mayor.")
else:
    print("Los dos numeros son iguales.")

print("-----------------------------")

#Ejercicio 3: Haz un programa que pida una calificacion del 0 al 10 y muestre si esta aprobado o reprobado. Toma en cuenta una calificacion mayor o igual a 6 como aprobatoria

nombreAlumno = input("Ingrese el nombre del alumno: ")
calificacion = float(input("Ingresa la calificacion del alumno (0 - 10:)"))

if calificacion >= 6:
    print:(f"El alumno {nombreAlumno} esta aprobado.")
else:
    print(f"El alumno {nombreAlumno} esta reprobado.")

    print("----------------------")

    #Ejercicio 4: Haz un programa que pida la edad de la persona y muestre si puede votar (mayor o igual a 18 años) o no

    nombre = input("Ingrese el nombre de la persona:")
    edadPersona = int(input("Ingresa su edad: "))

    if edadPersona >= 18:
        print(f"{nombre} tiene {edadPersona} años y puede votar.")
    else:
        print(f"{nombre} tiene {edadPersona} y no puede votar")
        