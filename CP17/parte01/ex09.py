class Moto:
    def __init__(self):
        self.marca = "Honda"
        self.modelo = "XRE 300"
        self.cor = "Vermelha"
        self.marcha = 4

    def imprimir(self):
        return f"Marca: {self.marca}, modelo: {self.modelo}, cor: {self.cor}, marcha: {self.marcha}"
    
moto = Moto()
print(moto.imprimir())