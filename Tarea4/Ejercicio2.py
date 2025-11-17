#Haz un programa que pida una frase y cuenta cuántas veces aparece cada palabra. Por ejemplo "Esta es una prueba", "Esta" aparece una vez, "es", una vez, "una", una vez, etc...

frase = input("Ingresa una frase: ")
palabras = frase.split()

conteo = {}

for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(conteo)
