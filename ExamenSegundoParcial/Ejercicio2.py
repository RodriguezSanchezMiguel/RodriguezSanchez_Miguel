#Pide una palabra y remplaza todas las vocales con el simbolo *

palabra = input("Ingresa una palabra: ").lower()
vocales = "aeiou"

for vocal in vocales:
    palabra = palabra.replace(vocal, "*")

print("Palabra nueva:", palabra)
