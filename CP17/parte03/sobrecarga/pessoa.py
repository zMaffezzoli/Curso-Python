class Pessoa:
    def __init__(self, codigo, nome, idade):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        print("Construtor padrão")

    def exibe(self):
        print(self.codigo)
        print(self.nome)
        print(self.idade)

    def exibe(self, numero):
        if numero == 1:
            print(self.codigo)
            print(self.nome)
            print(self.idade)

        else:
            print(self.codigo)
            print(self.nome)