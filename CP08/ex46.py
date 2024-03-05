def impressao(vetor):
    return vetor

def impressao_inversa(vetor):
    return vetor[::-1]

def media(vetor):
    return sum(vetor) / len(vetor)


vetor = [1, 2, 3, 4, 5, 6, 7]
print(impressao(vetor))
print(impressao_inversa(vetor))
print(media(vetor))