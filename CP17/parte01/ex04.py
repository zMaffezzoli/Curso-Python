class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        self.area = self.lado * self.lado

    def calcular_perimetro(self):
        self.perimetro = self.lado * 4

    def imprimir(self):
        return f'Lado: {self.lado}, Área: {self.area}, Perimetro: {self.perimetro}'
    


quadrado1 = Quadrado(5)
quadrado1.calcular_area()
quadrado1.calcular_perimetro()

print(quadrado1.imprimir())

quadrado2 = Quadrado(10)
quadrado2.calcular_area()
quadrado2.calcular_perimetro()

print(quadrado2.imprimir())