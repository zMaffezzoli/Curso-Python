class Eletrodomestico:
    def __init__(self, ligado):
        self.ligado = ligado

    def imprimir(self):
        return f"Ligado: {self.ligado}"

microondas = Eletrodomestico(False)

print(microondas.imprimir())

air_fryer = Eletrodomestico(True)

print(air_fryer.imprimir())