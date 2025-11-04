#Haz un programa que solicite números al usuario hasta que ingrese un cero. Al final, imprime cuántos números positivos y negativos introdujo

numero = int(input("Ingresa un numero ( o 0 para acabar con el programa): "))

numeros_positivos = 0
numeros_negativos = 0

while numero != 0:

    if numero > 0:
        numeros_positivos += 1
    else:
        numeros_negativos += 1

    numero = int(input("Ingresa un numero ( o 0 para acabar con el programa): "))

print(f"Los numeros positivos ingresados fueron {numeros_positivos} y los negativos fueron {numeros_negativos}")
