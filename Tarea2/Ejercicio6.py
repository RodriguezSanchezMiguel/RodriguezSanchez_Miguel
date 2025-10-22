#Haz un programa que pida tres numeros y muestre si se cumple la expresion A<B<C

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))

resultado = (num1 < num2) and (num2 < num3)

print(f'¿Secumple la preposicion? {resultado}')
