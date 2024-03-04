class Eletrodomestico:
    def __init__(self):
        self.ligado = False

    def imprimir(self):
        return f"Ligado: {self.ligado}"

microondas = Eletrodomestico()

print(microondas.imprimir())