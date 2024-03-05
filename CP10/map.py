def calcula_quadrado(n):
    return n ** 2

numeros = [2, 3, 4, 5, 6]
quadrados = []

for i in numeros:
    quadrados.append(calcula_quadrado(i)) # Em vez de fazer isso, podemos fazer com o map


quadrados = map(calcula_quadrado, numeros)
print(list(quadrados))
# Após a primeira utilização, a variavel/lista/tupla que à armazena é zerada
print(list(quadrados))