#Haz un programa que genera la tabla de multiplicar de un número ingresado. Al final, muestra cuantos resultados de las multiplicaciones fueron mayores que 50, cuántos menores que 50 y cuántos iguales a 50

numero = int(input("Ingresa un numero: "))
print(f"La tabla de multiplicar del {numero} es:")

contador_mayores_50 = 0
contador_menores_50 = 0
contador_iguales_50 = 0

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    if resultado > 50:
        contador_mayores_50 += 1
    elif resultado < 50:
        contador_menores_50 += 1
    else:
        contador_iguales_50 += 1

print(f"Resultados mayores que 50: {contador_mayores_50}")
print(f"Resultados menores que 50: {contador_menores_50}")
print(f"Resultados iguales a 50: {contador_iguales_50}")
