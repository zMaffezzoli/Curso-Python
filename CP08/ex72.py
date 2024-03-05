def soma_vetor(v1, v2, res):
    vetor = [v1, v2]

    vetor.insert(res-1, v1 + v2)

    return vetor


print(soma_vetor(3, 3, 1))
print(soma_vetor(6, 6, 2))
print(soma_vetor(2, 5, 3))