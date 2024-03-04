class Televisor:
    def __init__(self, ligado, canal, volume, numero_canais, volume_maximo):
        self.ligado = ligado
        self.canal = canal
        self.volume = volume
        self.numero_canais = numero_canais
        self.volume_maximo = volume_maximo

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def imprimir(self):
        return f"Ligado: {self.ligado}, canal sintonizado: {self.canal}, volume: {self.volume}, numero de canais: {self.numero_canais}, volume máximo: {self.volume_maximo}"
    
tv = Televisor(True, 10, 23, 33, 100)
print(tv.imprimir())

tv.desligar()
print(tv.imprimir())

tv.ligar()
print(tv.imprimir())