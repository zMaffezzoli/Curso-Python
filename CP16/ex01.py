class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    def exibe_dados(self):
        return f"Nome: {self.__nome}, idade: {self.__idade}, altura: {self.__altura}"
        

pessoa1 = Pessoa("Bernardo", 19, 1.80)

print(pessoa1.exibe_dados())

pessoa1.nome = "Bernnard"
pessoa1.idade = 20
pessoa1.altura = 1.82

print(pessoa1.exibe_dados())