# Reduce recebe dois parametros, função e dados, assim como map e filter

# Reduce realiza a função com os dois primeiros elementos dos dados(interavel) e depois aplica o resultado com o 3 elemento
# e assim por diante, até o último elemento

from functools import reduce

dados = [1, 2, 3, 4, 5]
funcao = lambda x, y: x * y

retorno = reduce(funcao, dados)
print(retorno)

# Mesma coisa disso

resultado = 1

for i in dados:
    resultado *= i

print(resultado)