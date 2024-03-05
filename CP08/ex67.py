def funcao(vetor, tamanho):
    
    soma = 0

    while True:
        digitado = input("Digite uma letra: ")
        soma += 1

        if digitado == "" or soma == tamanho:
            break

lista = [1, 2, 3, 4, 5, 6]
funcao(lista, len(lista))