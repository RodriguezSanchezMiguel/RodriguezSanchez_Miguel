#Haz un programa que pida un número, y muestre si es primo o no

numero = int(input("Ingresa un numero: "))

es_primo = True
if numero <= 1:
    es_primo = False
for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0:
        es_primo = False    
if es_primo:
    print("El numero es primo")
else:
    print("El numero no es primo")
