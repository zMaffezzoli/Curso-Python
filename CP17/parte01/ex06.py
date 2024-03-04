class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        self.area = self.comprimento * self.largura

    def calcular_perimetro(self):
        self.perimetro = (2 * self.comprimento) + (2 * self.largura)

    def imprimir(self):
        return f"Comprimento: {self.comprimento}, Largura: {self.largura}, Área: {self.area}, Perímetro: {self.perimetro}"
    

retangulo1 = Retangulo(15, 8)
retangulo1.calcular_area()
retangulo1.calcular_perimetro()

print(retangulo1.imprimir())