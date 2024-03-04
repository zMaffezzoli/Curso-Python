class Microondas:
    def __init__(self, ligado, porta_fechada):
        self.ligado = ligado
        self.porta_fechada = porta_fechada

    def ligar(self):
        if self.porta_fechada == True:
            self.ligado = True
            return f"Microondas ligado"
        else:
            return f"Porta está aberta"

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

print(microondas.ligar())
microondas.fechar_porta()
print(microondas.ligar())
print(microondas.imprimir())