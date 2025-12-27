#Hacer un registro de lumnos que pida nombre y edad, guardar en un archivo txt o csv, usar una clsae, agregar menu que tenga "agregar alumno y ver alumos"

import csv

class Alumno: 
    def __init__(self, nombre, edad, matricula):
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula

def agregar_alumno(nombre, edad, matricula) :
    with open("alumnos.csv", "a", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre,edad, matricula])
    print("Alumno agregado")

def ver_alumnos():
        with open("alumnos.csv", "r") as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if fila:
                    print(f"Nombre: {fila[0]}, Edad: {fila[1]}, Matricula: {fila[2]}")

def eliminar_alumno(matricula):
    alumnos = []
    eliminado = False

    with open("alumnos.csv", "r") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila and fila[2] != matricula:
                alumnos.append(fila)
            else:
                eliminado = True

    with open("alumnos.csv", "w", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(alumnos)
    
    print("Alumno eliminado")

def menu():
    while True:
        print("1. Agregar alumno")
        print("2. Ver alumnos")
        print("3. Eliminar alumno")
        print("4. Salir")

        opcion = input("Selecciona una opcion:")
            
        if opcion == "1":
            nombre = input("Ingresa el nombre completo del alumno: ")
            edad = input("Ingresa la edad del alumno: ")
            matricula = input("Ingresa la matricula del alumno: ")
            agregar_alumno(nombre, edad, matricula)

        elif opcion =="2":
            ver_alumnos()

        elif opcion == "3":
            matricula = input("Ingresa la matricula del alumno a eliminar: ")
            eliminar_alumno(matricula)

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion invalida, selecciona una de las opciones")

if __name__ == "__main__":
    menu()