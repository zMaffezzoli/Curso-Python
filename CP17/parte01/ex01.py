class Pessoa:
    def __init__(self):
        self.nome = "Anderson"
        self.endereco = "Rua Pereira, 456"
        self.telefone = "55 21 9 8984 7456"

    def imprimir(self):
        return f'{self.nome}, {self.endereco}, {self.telefone}'
    

p1 = Pessoa()

print(p1.imprimir())