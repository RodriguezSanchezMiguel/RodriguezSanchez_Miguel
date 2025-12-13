#For variable in terable 
#               Bloque de codigo

for i in range(0, 10, 2):
    print(i)

print("-----------------------------")

#ejercicio 1: Haz un programa que muestre los numeros del 1 al 20
print("Numeros del 1 al 20:")
for numero in range(1, 21):
    print(numero)

print("----------------------")

#Ejercicio 3: Haz un rograma que muestre la tabla de multiplicar de un numero dado por el usuario (del 1 al 10)

numero_usuario = int(input("Introduce un numero: "))
print(f"Tabla de multiplicar del {numero_usuario}:")
for i in range(1, 11):
    resultado = numero_usuario * i
    print(f'{numero_usuario} x {i} = {resultado}')

    print("------------------------")

    