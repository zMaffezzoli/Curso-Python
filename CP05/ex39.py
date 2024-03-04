salario_atual = float(input("Digite o salário atual do funcionário: "))
tempo_trabalho = float(input("Digite a quanto tempo esse funcionario trabalha(ano/anos): "))

if salario_atual <= 500:

    print(f"Reajuste sem bônus: {salario_atual*1.25}")

elif salario_atual > 500 and salario_atual <= 1000:

    if tempo_trabalho >= 1 and tempo_trabalho <= 3:
        print(f"Reajuste com bônus: R${salario_atual*1.20 + 100}")

    else:
        print(f"Reajuste sem bônus: R${salario_atual*1.20}")

elif salario_atual > 1000 and salario_atual <= 1500:
    
    if tempo_trabalho >= 4 and tempo_trabalho <= 6:
        print(f"Reajuste com bônus: R${salario_atual*1.15 + 200}")

    else:
        print(f"Reajuste sem bônus: R${salario_atual*1.15}")

elif salario_atual > 1500 and salario_atual <= 2000:

    if tempo_trabalho >= 7 and tempo_trabalho <= 10:
          print(f"Reajuste com bônus: R${salario_atual*1.10 + 300}")

    else:
        print(f"Reajuste sem bônus: R${salario_atual*1.10}")

else:

    if tempo_trabalho > 10:
        print(f"Sem reajuste, mas com bônus: R${salario_atual + 500}")

    else:
        print(f"Sem reajuste e sem bônus: R${salario_atual}")