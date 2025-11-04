#Haz un programa que sume todos los números impares del 1 al 50

numero = 50

suma_impares = 0

for i in range(1, 51):
    if i % 2 != 0:
        suma_impares += i

print(f"La suma de todos los numeros impares del 1 al {numero} es de {suma_impares}")
