# Funcion para buscar estudiante por medio del apellido 
def buscar_estudiantes_por_apellido(lista_estudiantes):
    apellido_buscar = input("Ingrese el apellido del estudiante que desea buscar: ")
    for estudiante in lista_estudiantes:
        if estudiante['apellido'].lower() == apellido_buscar.lower():
            print(f"Estudiante encontrado: {estudiante['apellido']} {estudiante['nombre']} - Promedio:{estudiante['promedio']}")
            return
        print("estudiante no encontrado.")

# Funcion para calcular el promedio del grupo
def calcular_promedio_grupo(lista_estudiantes):
    if not lista_estudiantes:
        print("No hay estudiantes en la lista para calcular el promedio.")
        return
    suma_promedios = sum(estudiante['promedio'] for estudiante in lista_estudiantes)
    promedio_grupo = suma_promedios / len(lista_estudiantes)
    print(f"El promedio del grupo es: {promedio_grupo:.2f}")


# Funcion para ordenar estudiantes por promedio (De la calificacion mas alta a la mas baja)
def ordenar_estudiantes_por_promedio(lista_estudiantes):
    lista_ordenada = sorted(lista_estudiantes, key= lambda v: v['promedio'], reverse=True)
    print("Estudiantes ordenados por promedio (de mayor a menor):")
    for estudiante in lista_ordenada:
        print(f"{estudiante['nombre']} {estudiante['apellido']} - Promedio: {estudiante['promedio']}")
