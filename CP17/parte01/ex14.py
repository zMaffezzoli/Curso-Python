class Moto:
    def __init__(self, marca, modelo, cor, marcha, menor_marcha, maior_marcha):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.marcha = marcha
        self.menor_marcha = menor_marcha
        self.maior_marcha = maior_marcha
        self.ligada = False

    def imprimir(self):
        return f"Marca: {self.marca}, modelo: {self.modelo}, cor: {self.cor}, marcha: {self.marcha}, maior marcha: {self.maior_marcha}, menor marcha: {self.menor_marcha}, ligada: {self.ligada}"
    
    def marcha_acima(self):
        if self.marcha == self.maior_marcha:
            return 'Já está na última marcha'
        
        self.marcha += 1
        return f"Marcha: {self.marcha}"
    
    def marcha_abaixo(self):
        if self.marcha == self.menor_marcha:
            return f'Já está na última marcha'

        self.marcha -= 1
        return f"Marcha: {self.marcha}"

moto = Moto("Honda", "CG 150", "Amarela", 3, 0, 6)

print(moto.marcha_acima())
print(moto.marcha_acima())
print(moto.marcha_acima())
print(moto.marcha_acima())
print(moto.marcha_abaixo())

print(moto.imprimir())
print()
moto2 = Moto("Honda", "CB300", "Preta", 2, -1, 3)
print(moto2.marcha_abaixo())
print(moto2.marcha_abaixo())
print(moto2.marcha_abaixo())
print(moto2.marcha_abaixo())
print(moto2.marcha_acima())

print(moto2.imprimir())
