#programa que pida un numero entero positivo y muestre su riaz cuadrda, raiz cubica
#potencia al cuadrado y potencia al cubo

import math

numero = int(input("Ingrese un numero entero positivo: "))

raizCuadrada = math.sqrt (numero)
raizCubica = numero ** (1/3)
potenciaCuadrado = pow(numero, 2)
potenciaCubica = pow(numero, 3)

print(f' La raiz cuadrada de {numero} es: {raizCuadrada}, ')
print(f'La raiz cubica de {numero} es: {raizCubica}, ')
print(f'La potencia al cuadrado de {numero} es: {potenciaCuadrado}, ')
print(f'La potencia cubica de {numero} es: {potenciaCubica}, ')
