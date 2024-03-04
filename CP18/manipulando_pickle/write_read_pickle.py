import pickle

nome = "Antônio"
idade = 12

with open('pessoa.pickle', 'wb') as arquivo:
    pickle.dump((nome, idade), arquivo)

with open('pessoa.pickle', 'rb') as arquivo:
    nome, idade = pickle.load(arquivo)
    print(nome, idade)