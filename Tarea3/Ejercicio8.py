#Pide dos números y muestra todos los números entre ellos que sean múltiplos de 7

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

if num1 > num2:
    num1, num2 = num2, num1

print("Los numeros multiplos de 7 entre", num1, "y", num2, "son los siguientes:")

for i in range(num1, num2 + 1):
    if i % 7 == 0:
        print(i)
