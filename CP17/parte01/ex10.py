class Moto:
    def __init__(self, marca, modelo, cor, marcha):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.marcha = marcha

    def imprimir(self):
        return f"Marca: {self.marca}, modelo: {self.modelo}, cor: {self.cor}, marcha: {self.marcha}"
    
moto = Moto("Honda", "CG 150", "Amarela", 3)
print(moto.imprimir())