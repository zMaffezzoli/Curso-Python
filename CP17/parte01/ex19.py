class Eletrodomestico:
    def __init__(self, ligado):
        self.ligado = ligado

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def imprimir(self):
        return f"Ligado: {self.ligado}"

microondas = Eletrodomestico(False)
print(microondas.imprimir())
microondas.ligar()
print(microondas.imprimir())

print()

air_fryer = Eletrodomestico(True)
print(air_fryer.imprimir())
air_fryer.desligar()
print(air_fryer.imprimir())