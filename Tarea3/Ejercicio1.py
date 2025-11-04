#Haz un programa que calcule cuántos números del 1 al 100 son divisibles entre 3 y entre 5

numero = 100
numeros_divisibles = 0

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        numeros_divisibles += 1
print(f"Los numeros del 1 al 100 que son divisibles entre 3 y 5 son: {numeros_divisibles}")
