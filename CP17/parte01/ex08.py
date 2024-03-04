class Circulo:

    pi = 3.141516

    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        self.area = Circulo.pi * self.raio * self.raio

    def calcular_perimetro(self):
        self.perimetro = 2 * Circulo.pi * self.raio

    def imprimir(self):
        return f"Raio: {self.raio}, Área: {self.area}, Perímetro: {self.perimetro}"
    

circulo1 = Circulo(7)
circulo1.calcular_area()
circulo1.calcular_perimetro()

print(circulo1.imprimir())