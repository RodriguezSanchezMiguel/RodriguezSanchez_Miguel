#Haz un programa que pida la frase y cuenta cuantas letras tiene la frase, sin contar espacios

frase = input("Ingresa una frase: ").lower()
contador = 0

for caracter in frase:
    if caracter != " ":
        contador += 1

print("La frase tiene ", contador, "letras (sin contar espacios).")
