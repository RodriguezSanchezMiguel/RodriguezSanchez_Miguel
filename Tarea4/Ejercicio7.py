#Haz un programa en Python que pida repetidamente el nombre de una persona y su respuesta ("Si" o "No"). Guarda cada respuesta en un diccionario, donde la clave sea el nombre y el valor la respuesta. El programa debe terminar cuando el usuario escriba "Fin" como nombre. Al finalizar, muestra cuántas personas respondieron "Si", y cuántas respondieron "No"


def main():
    respuestas = {}

    while True:
        nombre = input("Ingresa el nombre de la persona (o Fin para terminar): ").strip()
        if nombre.lower() == "fin":
            break

        respuesta = input("Escribe la respuesta (Si/No): ").strip()
        while respuesta.lower() not in ("si", "no"):
            respuesta = input("Respuesta inválida. Escribe 'Si' o 'No': ").strip()

        respuestas[nombre] = "Si" if respuesta.lower() == "si" else "No"

    contador = {"Si": 0 , "No": 0}
    for v in respuestas.values():
        if v == "Si":
            contador["Si"] += 1
        else:
            contador["No"] += 1

    print()
    print(f"Personas que respondieron 'Si': {contador['Si']}")
    print(f"Personas que respondieron 'No': {contador['No']}")

if __name__ == "__main__":
    main()
