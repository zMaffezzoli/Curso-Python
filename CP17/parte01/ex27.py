class Microondas:
    def __init__(self, ligado):
        self.ligado = ligado
    def imprimir(self):
        return f"Ligado: {self.ligado}"
    
microondas = Microondas(False)
print(microondas.imprimir())