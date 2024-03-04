class Microondas:
    def __init__(self):
        self.ligado = True

    def imprimir(self):
        return f"Ligado: {self.ligado}"
    
microondas = Microondas()
print(microondas.imprimir())