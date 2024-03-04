class Televisor:
    def __init__(self, ligado, canal, volume):
        self.ligado = ligado
        self.canal = canal
        self.volume = volume

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def imprimir(self):
        return f"Ligado: {self.ligado}, canal sintonizado: {self.canal}, volume: {self.volume}"
    
tv = Televisor(True, 10, 23)
print(tv.imprimir())

tv.desligar()
print(tv.imprimir())

tv.ligar()
print(tv.imprimir())