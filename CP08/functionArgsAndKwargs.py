def exemplo(*args):  # Retorna uma tupla com todos os parametros extras passados
    return sum(args) 

print(exemplo(1,2,3,4,5,7, *[1,2,3]))

#print(exemplo(1,2,3,4,5,7, [1,2,3])) # Dará erro, pois precisa retirar os números da lista, feito acima


def exemplo2(**kwargs): # Mesma coisa do args, porém retorna dicionário
    return kwargs

print(exemplo2(pessoa="Bonita", idade=10))

# def minha_funcao(nome, idade, *args, maior_idade=False, **kwargs): Fazer nesta ordem caso a função possua todos os parâmetros

def exemplo3(nome, idade, *args):
    return f"Seu nome é {nome}, tem {idade} anos e valores extras{args}"

print(exemplo3("Marcos", 12, 2, 3, 5, [1,2], "Sei lá"))