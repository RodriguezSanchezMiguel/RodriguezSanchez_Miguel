#Haz un programa que pida al usuario solicitar 5 calificaciones, solo acepta numeros del 1 al 10 (si se permite decimales). Almacena estas 5 calificaciones en un arreglo y posteriormente cacula el promedio de las calificaciones muestra solamente 2 decimales. Si el alumno tiene una calificacion promedio mayor que 6 imprime un mensaje de "Aprobado" si tiene una calificacion menor que 6 imprime "Reprobado" y si tiene una calificacion de 10 imprime "Excelente"


calificaciones = []

for i in range(5):
    while True:
            calificacion = float(input(f"Ingresa la calificación {i+1} (entre 1 y 10): "))
            if 1 <= calificacion <= 10:
                calificaciones.append(calificacion)
                break
            else:
                print("Error: La calificación debe estar entre 1 y 10.")
        

promedio = sum(calificaciones) / len(calificaciones)
promedio = round(promedio, 2)
print(f"El promedio es: {promedio}")

if promedio == 10:
    print("Excelente")
elif promedio >= 6:
    print("Aprobado")
else:
    print("Reprobado")
    