#Haz un programa que pida un número y muestre si es divisible entre 2, 3 o ambos

numero = int(input("Ingresa un numero: "))

if numero % 2 == 0 and numero % 3 == 0:
    print(f"El numero {numero} es divisible entre 2 y 3")
elif numero % 2 == 0:
    print(f"El numero {numero} solo es divisible entre 2")
elif numero % 3 == 0:
    print(f"El numero {numero} solo es divisible entre 3")
else:
    print(f"El numero {numero} no es divisible ni entre 2 ni entre 3")
