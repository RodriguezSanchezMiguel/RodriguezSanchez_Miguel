#Haz un programa que pida un texto y una palabra. Si la palabra está en el texto, muestra cuántas veces aparece.

texto = input("Ingresa un texto: ").lower()
palabra = input("Ingresa una palabra: ").lower()

palabras = texto.split()

conteo = {}

for p in palabras:
    conteo[p] = conteo.get(p, 0) + 1

if palabra in conteo:
    print(f"La palbra '{palabra}' aparece {conteo[palabra]} veces en el texto {texto}")

else:
    print(f"LA palabra '{palabra}' no aparece en el texto {texto}")
