#Haz un programa que sume todos los números pares del 1 al 100. Al final muestra el resultado de la suma

numero = 100
suma_pares = 0

for i in range(0, 101, 2):
    suma_pares += i

print(f"La suma de todos los numeros pares del 1 al {numero} es: {suma_pares}")
