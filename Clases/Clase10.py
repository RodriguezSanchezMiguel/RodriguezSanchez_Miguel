# Metodos de utilidad
lista_frutas = ["manzana", "banana", "cereza", "durazno", "naranja"]
print(lista_frutas)

lista_frutas.append("kiwi")# Agrega un elemento al final de la lista
print(lista_frutas)

lista_frutas.pop()# Elimina el ultimo elemento de la lista
print(lista_frutas)

lista_frutas.pop(2)# Elimina el elemento en la posicion 2 (tercer elemento)
print(lista_frutas)

lista_frutas.remove("banana")# Elimina el elemento con el valor "banana"
print(lista_frutas)

lista_frutas.insert(2, "uva")# Inserta el elemento "uva" en la posicion 2 (tercer lugar)
print(lista_frutas)

lista_frutas.clear()# Elimina todos los elementos de la lista
print(lista_frutas)

lista_frutas = []# Reinicia la lista para los siguientes ejercicios
print(lista_frutas)

lista_frutas = ["manzana", "banana", "cereza", "durazno", "naranja"]
lista_frutas.index("cereza")# Devuelve la posicion del elemento "cereza"
print(lista_frutas.index("cereza"))

lista_frutas.count("banana")# Cuenta cuantas veces aparece "banana" en la lista
print(lista_frutas.count("banana"))

lista_frutas.sort()# Ordena la lista alfabeticamente
print(lista_frutas)

lista_frutas.reverse()# Invierte el orden de la lista
print(lista_frutas)

len(lista_frutas)# Devuelve la cantidad de elementos en la lista
print(len(lista_frutas))

lista = [5, 2, 9, 1, 5, 6]
print(sum(lista))# Devuelve la cantidad de elementos en la lista

# Ejercicio 1: Pide 5 numeros, guerdalos en una lista y muestra el promedio y el mayor de los numeros
lista_numeros = []

for i in range(5):
    numero = float(input("Ingresa un numero: "))
    lista_numeros.append(numero)

promedio = sum(lista_numeros) / len(lista_numeros)
num_mayor = max(lista_numeros)

print(f"El promedio de los numeros ingresados es: {promedio} y el numero mayor es: {num_mayor}")

# Ejercicio 2: Pide numeros hasta que el usuario escriba 0; guardalos en una lista y muestra la lista ordenada ascendentemente
lista_numeros = []
while True:
    numero = float(input("Ingresa un numero (Ingresa 0 para terminar): "))
    if numero == 0:
        break   
    lista_numeros.append(numero)

lista_numeros.sort()
print("La lista ordenada:", lista_numeros)

