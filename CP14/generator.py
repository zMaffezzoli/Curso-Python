def conta(numero):
    contador = 1
    while contador <= numero:
        yield contador # Faz com que a função retorne múltiplas vezes. Ela gera um generator, que sempre é um iterator
        contador += 1

minha_func = conta(10)

for i in minha_func:
    print(i)