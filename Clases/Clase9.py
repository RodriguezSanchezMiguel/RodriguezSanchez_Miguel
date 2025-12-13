#Ejercicio 3: Haz un programa que pida nombre y apellido .Muestra en pantalla en formato apellido. nombre con cada palabra iniciando en mayuscula
nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")
nombre_completo = apellido + "," + nombre

print(nombre_completo.title())

#Ejercicio 4: Pide una frase y una letra y muestra cuantas veces aparece esa letra en la frase sin distinguir entre mayusculas y minusculas
frase = input("Ingresa una frase: ")
letra = input("Escribe la letra que deseas buscar: ")
frase_formateada = frase.strip().lower()
letra_formateada = letra.strip().lower()

conteo_letra = frase_formateada.count(letra_formateada)

print(f"La letra {letra} aparece {conteo_letra} veces en la frase: {frase}")

#Ejercicio 5: Pide una frase y remplaza todas las bocales 'a' por '@' y  muestra el resultado

frase = input("Ingresa una frase: ")
frase_formateada = frase.strip().lower()
frase_modificada = frase_formateada.replace("a", "@")

print("Frase modificada:", frase_modificada)

#Ejercicio 6: Pide un texto y extrae los primeros 10 caracteres. Si el texto tiene menos de 10 caracteres, muestra el texto completo

texto = input("Ingresa un texto: ")
if len(texto) <= 10:
    print(f"El texto completo es: {texto}")
else:
    texto_diez_caracteres = texto[:10]
    print(f"Los primeros 10 caracteres son: {texto_diez_caracteres}")
    
#LISTAS EN PYTHON
lista1 = [10, 30, 20, 50, 5, 15,]
lista2 = ["manzana", "banana", "fresa", "pera", "naranja", 4, 6.6, True]

print(lista1)
print(lista2)

for elemento in lista1:
    print(elemento)

for elemento in lista2:
    print(elemento)

#Llenado de listas vacias
lista3 = [] #Lista vacia
#Llenar la lista con datos ingresados por el usuario
for i in range(11):
    numero = int(input("Ingresa un numero entero: "))
    lista3.append(numero)#El append agrega el numero ingresado al final de la lista
print("Lista llena:", lista3)

print(len(lista3))#Imprime la longitud de la lista
print(sum(lista3))#Imprime la suma de todos los elementos de la lista

print(lista3.reverse())#invierte el orden de los numeros
print("Lista invertida:", lista3)
print(lista3.sort())#Ordena los elemnetos de la lista en orden ascendente
print("Lista ordenada:", lista3)
