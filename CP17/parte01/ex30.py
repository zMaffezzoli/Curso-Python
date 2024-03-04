class Microondas:
    def __init__(self, ligado, porta_fechada):
        self.ligado = ligado
        self.porta_fechada = porta_fechada

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def abrir_porta(self):
        self.porta_fechada = False

    def fechar_porta(self):
        self.porta_fechada = True

    def imprimir(self):
        return f"Ligado: {self.ligado}, porta fechada: {self.porta_fechada}"
    
microondas = Microondas(False , False)
print(microondas.imprimir())

microondas.fechar_porta()
print(microondas.imprimir())

microondas.abrir_porta()
print(microondas.imprimir())