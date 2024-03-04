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

    def canal_acima(self):
        if self.canal == self.numero_canais:
            self.canal = 1
        else:
            self.canal += 1

    def canal_abaixo(self):
        if self.canal == 1:
            self.canal = self.numero_canais
        else:
            self.canal -= 1

    def imprimir(self):
        return f"Ligado: {self.ligado}, canal sintonizado: {self.canal}, volume: {self.volume}, numero de canais: {self.numero_canais}, volume máximo: {self.volume_maximo}"
    
tv = Televisor(True, 10, 23, 12, 100)
print(tv.imprimir())

tv.canal_acima() # Canal 11
tv.canal_acima() # Canal 12
tv.canal_acima() # Canal 1

tv.canal_abaixo() # Canal 12
tv.canal_abaixo() # Canal 11
print(tv.imprimir())