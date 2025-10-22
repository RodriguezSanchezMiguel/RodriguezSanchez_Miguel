# Haz un programa que pida numeros y muestre si el primero es mayor, menor o igual al segundo 

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero numero: "))

resultado1 = (num1 < num2)
resultado2 = (num1 > num2)
resultado3 = (num1 == num2)

print(f'El primer numero es mayor que el segundo {resultado1}')
print(f'El primer numero es menor que el segundo {resultado2}')
print(f'El primer numero es igual que el segundo {resultado3}')
