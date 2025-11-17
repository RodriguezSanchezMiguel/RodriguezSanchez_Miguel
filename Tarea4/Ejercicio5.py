#Pide al usuario una lista de palabras (separadas por comas, por ejemplo Hola, Mario, Python, Programación). Elimina los elementos repetidos y los que sean menores a 3 letras. Muestra la nueva lista e imprímela en pantalla. 

lista_palabras = [palabra.strip() for palabra in input("Ingresa una lista de palabras separadas por comas: ").split()]

lista_sin_duplicados = list(set(lista_palabras))

lista_filtrada = [palabra for palabra in lista_sin_duplicados if len(palabra) >=3]
print("lista consumada:", lista_filtrada)
