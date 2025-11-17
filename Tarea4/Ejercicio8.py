#Haz un programa que pida una palabra y verifique si inicia con una vocal.

palabra = input("Ingresa un palabra: ").lower()
vocales = "aeiou"

if palabra[0] in vocales:
    print(f"La palabra {palabra} si inicia con una vocal")
else:
    print(f"La palabra {palabra} no inicia con una vocal")
