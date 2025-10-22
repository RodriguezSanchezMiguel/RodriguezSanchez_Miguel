#Haz un programa que pida tres calificaciones y calcule su promedio con dos decimales

Calificacion1 = int(input("Ingresa la primera calificacion: "))
Calificacion2 = int(input("Ingresa la segunda calificacion: "))
Calificacion3 = int(input("Ingresa la tercera calificacion: "))

promedio = ((Calificacion1 + Calificacion2 + Calificacion3)/3)

print("El promedio es: ", round(promedio, 2))
