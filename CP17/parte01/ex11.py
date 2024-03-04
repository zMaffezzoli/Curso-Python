class Moto:
    def __init__(self, marca, modelo, cor, marcha):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.marcha = marcha

    def imprimir(self):
        return f"Marca: {self.marca}, modelo: {self.modelo}, cor: {self.cor}, marcha: {self.marcha}"
    
    def marcha_acima(self):
        self.marcha += 1
        return f"Marcha: {self.marcha}"
    
    def marcha_abaixo(self):
        self.marcha -= 1
        return f"Marcha: {self.marcha}"

moto = Moto("Honda", "CG 150", "Amarela", 3)

print(moto.marcha_acima())
print(moto.marcha_acima())
print(moto.marcha_acima())
print(moto.marcha_abaixo())

print(moto.imprimir())
print()
moto2 = Moto("Honda", "CB300", "Preta", 2)
print(moto2.marcha_abaixo())
print(moto2.marcha_abaixo())
print(moto2.marcha_abaixo())
print(moto2.marcha_acima())

print(moto2.imprimir())
