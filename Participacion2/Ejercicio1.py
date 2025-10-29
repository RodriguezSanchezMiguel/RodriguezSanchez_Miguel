# Haz un programa en Python que pida un número, posteriormente muestra todos los números desde 1 hasta el número ingresando. Imprime en consola un coteo de números pares y de números impares

numero = int(input("Ingresa un numero: "))

numeros_pares = 0
numeros_impares = 0

for i in range(1, numero + 1):
    if i % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1
    print(i)

print(f"Hay {numeros_pares} numeros pares y {numeros_impares} numeros impares del 1 hasta el {numero}")
