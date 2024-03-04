nota = float(input("Digite a nota do aluno: "))
faltas = int(input("Digite a qunatidade de faltas do aluno: "))

reducao = faltas<=20

if nota >= 9 and nota <= 10:
    if reducao:
        print("A")

    else:
        print("B")

elif nota >= 7.5 and nota <= 8.9:
    if reducao:
        print("B")
    
    else:
        print("C")

elif nota >= 5.0 and nota <= 7.4:
    
    if faltas <= 20:
        print("C")

    else:
        print("D")

elif nota >= 4.0 and nota <= 4.9:
    if faltas <= 20:
        print("D")

    else:
        print("E")

else:
        print("E")