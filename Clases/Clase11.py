# Ejercicio 3: Pide 6 nombres y muestra la lista numerada (1. Nombre1, 2. Nombre2, etc)

lista_nombres = []
for i in range(6):
    nombre = input("Ingrese su nombre: ")
    lista_nombres.append(nombre)

lista_nombres.sort()

for i, nombre in enumerate (lista_nombres, start=1):
    print(f"{i}. {nombre}")


# Ejercicio 4: Pide 8 numeros, elimina las repeticiones y muestra la lista sin duplicados ordenados de mayor a menor

lista_numeros = []
for i in range(8):
    numero = int(input("Ingresa un numero: "))
    lista_numeros.append(numero)

lista_numeros_ordenados = list(set(lista_numeros))
lista_numeros_ordenados.sort()
print(lista_numeros_ordenados)

# Ejercicio 5: Pide 10 calificaciones entre 0 y 10. Si alguna es menor que 0, añade al conteo de reprobados. Al final, muestra cuantos aprobaron y cuantos reprobaron.

lista_aprobados = []
lista_reprobados = []

for i in range(10):
    calificacion = float(input("Ingresa una calificacion: "))
    while(calificacion < 0 or calificacion > 10):
        calificacion = float(input("Calificacion invalida. Introduce una calificacion entre 0 y 10"))
if calificacion < 6:
    lista_reprobados.append(calificacion)
else:
    lista_aprobados.append(calificacion)

print(f"Cantidad de aprobados: {len(lista_aprobados)}")
print(f"Cantidad de repobados: {len(lista_reprobados)}")

# Diccionarios

diccionario = {
    "nombre": "Mario",
    "apellido": "Segovia",
    "edad": 29,
    "licenciatura": "Ingeniero en Sistemas Computacionales",
    "isEmpleado": True
}

print(diccionario.keys()) #Devuelve las claves del diccionario
print(diccionario.values()) #
print(diccionario.items())
print(diccionario["isEmpleado"])
diccionario.pop("edad")
print(diccionario) 
print(len(diccionario))   

diccionario["edad"] = 29 #Agregar o Actualizar un valor
print(diccionario)

# Recorrer un diccionario 
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")

# Ejercicio 1: Crea un diccionario vacio. Pide nombres y calificaciones de 5 alumnos y guardalos en el diccionario. Lego muestra su promedio
diccionario_alumnos = []
for i in range(5):
    nombre = input("Ingresa el nombre del alumno: ")
    calificacion = float(input("Ingresa la calificacion del alumno: "))
    while(calificacion < 0 or calificacion > 10):
        calificacion = float(input("Calificacion invalida. Introduce la calificacion de {nombre} entre0 y 10: "))
    diccionario_alumnos[nombre] = calificacion

print(diccionario_alumnos)

for clave, valor in diccionario_alumnos.items():
    print(f"La calificacion de {clave} es: {valor}")

suma_calificaciones = sum(diccionario_alumnos.values())
promedio = suma_calificaciones / len(diccionario_alumnos)
print(f"El promedio de las calificaciones es: {promedio}")

# Ejercicio 2: Crea un diccionario con 5 productos y sus precios. Pide un producto y muestra su precio
diccionario_productos = {
    "Cloro": 20,
    "Detergente": 35,
    "Jabon": 15,
    "Papel sanitario": 40,
    "Limpiador multiusos": 60
}
producto_buscado = input("Introduce el nombre del producto: ")
if producto_buscado in diccionario_productos:
    print(f"El precio de {producto_buscado} es: ${diccionario_productos}[producto_buscado].")
else:
    print("El producto no se encuentra en el inventario")

# Ejercicio 3: Crea un diccionario con 5 paises y sus capitales. Pide un pais y muestra su capital

pais_buscado = input("Introduce el nombre del pais o 'Salir' para terminar: ")
diccionario_paises = {
    "Mexico": "Ciudad de mexico",
    "Brazil": "Brasilia",
    "Uruguay": "Monte video",
    "Argentina": "Buenos aires",
    "Estados unidos": "Washinton D.C"
}
while pais_buscado != "Salir":
    if pais_buscado in diccionario_paises:
        print(f"La capital del pais {pais_buscado} es: {diccionario_paises} [pais_buscado]")
    else:
        capital_pais = input("El pais no se encuentra en el diccionario. Introduce la capital de ese pais: ")
        diccionario_paises = [pais_buscado] = capital_pais
        