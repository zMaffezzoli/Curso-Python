nota100 =  0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0

valor = int(input("Digite o valor do saque(inteiro): "))

while True:

    if valor >= 100:
        valor -= 100
        nota100 += 1

    elif valor >= 50:
        valor -= 50
        nota50 += 1

    elif valor >= 20:
        valor -= 20
        nota20 += 1

    elif valor >= 10:
        valor -= 10
        nota10 += 1

    elif valor >= 5:
        valor -= 5
        nota5 += 1

    elif valor >= 2:
        valor -= 2
        nota2 += 1

    elif valor >= 1:
        valor -= 1
        nota1 += 1

    else:
        break

print(f"Serão necessárias {nota100} notas de 100, {nota50} notas de 50, {nota20} notas de 20, {nota10} notas de 10, {nota5} notas de 5, {nota2} notas de 2 e {nota1} notas de 1")