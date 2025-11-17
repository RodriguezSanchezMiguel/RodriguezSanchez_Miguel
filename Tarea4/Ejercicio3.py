#Haz un programa que pida al usuario una contraseña. Verifica que: La contraseña tenga al menos 8 caracteres, y que contenga al menos una mayúscula y un número.

def es_valido(contrasena):
    tiene_numero = any(char.isdigit() for char in contrasena)
    tiene_mayuscula = any(char.isupper() for char in contrasena)
    return len(contrasena) >= 8 and tiene_numero and tiene_mayuscula

contrasena = input("Ingresa la contraseña: ")

if es_valido(contrasena):
    print("Contraseña valida")
else:
    print("Contraseña invalida")
