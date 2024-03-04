class Microondas:
    def __init__(self, ligado):
        self.ligado = ligado

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def imprimir(self):
        return f"Ligado: {self.ligado}"
    
microondas = Microondas(False)
microondas.ligar()
print(microondas.imprimir())
microondas.desligar()
print(microondas.imprimir())