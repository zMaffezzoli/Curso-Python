class Microondas:
    def __init__(self, ligado, porta_fechada):
        self.ligado = ligado
        self.porta_fechada = porta_fechada

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def imprimir(self):
        return f"Ligado: {self.ligado}, porta fechada: {self.porta_fechada}"
    
microondas = Microondas(False , True)
microondas.ligar()
print(microondas.imprimir())
microondas.desligar()
print(microondas.imprimir())