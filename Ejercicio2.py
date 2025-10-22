# Haz un programa que pida tres numeros enteros y muestre si se cumple la expresion: Elprimer numero es mayor que el segundo y el segundo menor que el tercero. Esto sin utilizar condiciones, solo operadores logicos.

num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))
num3 = int(input("Ingrese el tercer numero entero: "))

resultado = (num1 > num2) and (num2 < num3)

print(f'¿Se cumple la proposicion? {resultado}')
