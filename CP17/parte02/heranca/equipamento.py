class Equipamento:
    def __init__(self, preco, ano_lancamento):
        self.__preco = preco
        self.__ano_lancamento = ano_lancamento

    @property
    def preco(self):
        return self.__preco
    
    @property
    def ano_lancamento(self):
        return self.__ano_lancamento
    
    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @ano_lancamento.setter
    def ano_lancamento(self, ano_lancamento):
        self.__ano_lancamento = ano_lancamento

    def exibe(self):
        print(self.__preco)
        print(self.__ano_lancamento)