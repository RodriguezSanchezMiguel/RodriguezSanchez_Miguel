#Pide una frase, divídela en palabras y guarda una lista solo las que tengan más de 5 letras. Muestra la lista resultante.

frase = input("Ingrese una frase: ").lower()
palabras = frase.split()

palabras_grandes = []

for p in palabras:
    if len(p) > 5:
        palabras_grandes.append(p)
print("Las palabras que tienen mas de 5 letras son:", palabras_grandes)
