velha = [[-1, 1, 0], [-1, -1, 1], [0, 1, 0]]

for linha in range(3):
    for elemento_coluna in range(3):

        if (velha[linha][elemento_coluna] == 0 and sum(velha[linha]) == -2) or (velha[linha][elemento_coluna] == 0 and sum(velha[linha]) == -1) or (velha[linha][elemento_coluna] == 0 and sum(velha[linha]) == 0) or (velha[linha][elemento_coluna] == 0):
            print(f"Deve colocar na posição linha: {linha + 1} coluna: {elemento_coluna + 1}")
            break