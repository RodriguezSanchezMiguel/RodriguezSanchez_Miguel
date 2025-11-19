#Haz un programa que pida una palabra y cuenta cuatas vocales tiene la palabra ingresada 

palabra = input("Ingresa una palabra: ").lower()
vocales = "aeiou"
contador = 0

for vocal in vocales:
    contador += palabra.count(vocal)

print(f"La palbra '{palabra}' tiene {contador} vocales")
