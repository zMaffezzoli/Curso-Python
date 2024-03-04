class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def imprimir(self):
        return f'{self.nome}, {self.endereco}, {self.telefone}'
    

pesso1 = Pessoa("Anderson", "Rua Pereira, 456", "55 21 9 8984 7456")
print(pesso1.imprimir())