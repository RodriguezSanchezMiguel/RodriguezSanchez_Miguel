# Calculadora de salario semanal

# Solicitar al usuario los dias trabajados
dias = int(input("Ingrese los dias trabajados: "))

# Conversion del salario
conversionSalario = (dias * 120)

# Verificar si hay horas extras
if dias >= 5:
    print("hiciste horas extras, tu salario es de:", [conversionSalario])
else:
    print("tu salario es de:", [conversionSalario])

