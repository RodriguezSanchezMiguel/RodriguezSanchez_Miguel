nombre = "Mario Alonso Segovia Gutierrez"
cadena2 = "Hola a todos mi nombre es mario alonso segovia gutierrez"
cadena3 = "                Hola mundo          "
cadena4 = "Esta es la cadena 4"
cadena5 = "Esta es la cadena 5"
cadena6 = "Hola ¿como estas? ¿Estas bien?"
cadena7 = "Anita lava la tina"

print(len(nombre))#Imprime la longitud de la cadena 

print(nombre.upper())#Convierte la cadena a mayúsculas

print(nombre.lower())#Convierte la cadena a minúsculas

print(cadena2.capitalize())#Convierte la primera letra de la cadena a mayúscula

print(cadena2.title())#Convierte la primera letra de cada palabra a mayúscula

print(cadena3.strip())#Elimina los espacios en blanco al inicio y al final de la cadena

cadenaNueva = cadena4 + cadena5
print(cadenaNueva)#Concatenacion de cadenas

cadenaMultiplicada = cadena4 * 5
print(cadenaMultiplicada)#Multiplicacion de cadenas

print(cadena4.replace("a", "s"))#Remplaza todas las apariciones de "a" por "s"

indice = cadena6.find("¿")#Busca la primera aparicion del caracter "¿" 
print(indice)#Imprime la posicion de la primera aparicion de "¿"

indiceUltimo = cadena6.rfind("¿")#Busca la ultima aparicion del caracter "¿"
print(indiceUltimo)#Imprime la posicion de la ultima aparicion de "¿"

conteo = cadena7.count("a")#Cuenta cuantas veces aparece el caracter "a"
print(conteo)#Imprime el conteo de apariciones de "a"

print(cadena7.startswith("Anita"))#Verifica si la cadena empieza con "Anita"
print(cadena7.endswith("tina"))#Verifica si la cadena termina con "tina"
print(cadena7.isalpha())#Verifica si la cadena solo contiene letras
print(cadena6.isalnum())#Verifica si la cadena solo contiene letras y numeros
print(cadena6.split(" "))#Divide la cadena en una lista usando el espacio como separador
print("-".join(cadena7))#Une los caracteres de la cadena con "-" como separador
print(cadena4.center(30, "*"))#Centra la cadena en un espacio de 30 caracteres rellenando con "*"
print(cadena4.ljust(30, "-"))#Alinea la cadena a la izquierda en un espacio de 30 caracteres rellenando con "-"
print(cadena4.rjust(30, "+"))#Alinea la cadena a la derecha en un espacio de 30 caracteres rellenando con "+"
print(cadena4.zfill(30))#Rellena la cadena con ceros a la izquierda hasta tener una longitud de 30 caracteres
print(cadena4.encode("utf-8"))#Codifica la cadena en bytes usando utf-8
print(cadena4.partition("cadena"))#Divide la cadena en una tupla usando "cadena" como separador
print(cadena4.expandtabs(4))#Reemplaza los tabuladores por espacios (4 espacios por tabulador)
print(cadena4.swapcase())#Invierte las mayúsculas y minúsculas de la cadena
print(cadena4.translate(str.maketrans("aeiou", "12345")) )#Reemplaza las vocales por numeros segun el mapeo dado
print(cadena4.isupper())#Verifica si todas las letras de la cadena son mayúsculas
print(cadena4.islower())#Verifica si todas las letras de la cadena son minúsculas
print(cadena4.istitle())#Verifica si la cadena está en formato título (primera letra de cada palabra en mayúscula)
print(cadena4.removeprefix("Esta"))#Elimina el prefijo "Esta" de la cadena si está presente
print(cadena4.removesuffix("5"))#Elimina el sufijo "5" de la cadena si está presente
print(cadena4.count("e", 0, 10))#Cuenta cuantas veces aparece "e" entre los indices 0 y 10
print(cadena4.index("c"))#Busca la primera aparicion del caracter "c" y devuelve su indice
print(cadena4.rindex("a"))#Busca la ultima aparicion del caracter "a" y devuelve su indice

#Sintaxis de Slicing cadena[inicio:fin:paso]

cadena8 = "Hola a todos"
print(cadena8[0:4])#Imprime "Hola"
print(cadena8[:4])#Imprime "Hola"
print(cadena8[4:9])#Imprime "a to"
print(cadena8[5:])#Imprime "a todos"
print(cadena8[-2:])#Imprime "os"
print(cadena8[::2])#Imprime "Hla tds"
print(cadena8[::-1])#Imprime "sodot a aloH"

#Ejercicio 1: Pide una frase y muestra la misma frase sin espacios al inicio y al final con todas las letras en minusculas

frase = input("Escribe una frase: ")
fraseLimpia = frase.strip().lower()
print(fraseLimpia)

#Ejercicio 2: Pide una palabra y comprueba si es un palindromo

palabra = input("Escribe una palabra: ")
palabra_invertida = palabra[::-1]
if palabra.lower() == palabra_invertida.lower():
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")

palabra = "Palabra ejemplo"

for letra in palabra:
    print(letra)