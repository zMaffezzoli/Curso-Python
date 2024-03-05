pessoas = ["Aline", "Pedro", "Bianca", "José", "João", "Tim", "Olivandro"]

print(max(pessoas)) # Pega o maior por ordem alfabética

print(max(pessoas, key=lambda pessoa: len(pessoa))) # Pega o maior por tamanho

print(min(pessoas)) # Pega o menor por ordem alfabética

print(min(pessoas, key=lambda pessoa: len(pessoa))) # Pega o menor por tamanho