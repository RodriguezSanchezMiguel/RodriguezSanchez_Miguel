#Haz un programa que simule una calculadora básica con opciones de suma, resta, multiplicación y división, que se repita hasta que el usuario elija salir

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

opcion = 0

while opcion != 5:
    print("Selecciona la operación que quieras hacer:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

    opcion = int(input("Escoge una opcion (1-5): "))

    if opcion == 1:
        resultado = num1 + num2
        print(f"La suma de {num1} y {num2} es: {resultado}")
    elif opcion == 2:
        resultado = num1 - num2
        print(f"La resta de {num1} y {num2} es: {resultado}")
    elif opcion == 3:
        resultado = num1 * num2
        print(f"La multiplicación de {num1} y {num2} es: {resultado}")
    elif opcion == 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"La división de {num1} entre {num2} es: {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")
    else:
        print("Saliendo de la calculadora. ¡Hasta luego!")
        
