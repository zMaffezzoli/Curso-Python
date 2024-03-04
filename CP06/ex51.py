salario_1995 = 2000

aumento = 1.5
salario_1996 = salario_1995 * aumento

for i in range(2024 - 1996):
    aumento *= 2

    salario_atual = salario_1996*aumento

print(salario_atual)