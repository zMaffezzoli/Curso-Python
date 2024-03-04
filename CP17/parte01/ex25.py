class Televisor:
    def __init__(self, ligado, canal, volume, volume_maximo, numero_canais):
        self.ligado = ligado
        self.canal = canal
        self.volume = volume
        self.volume_maximo = volume_maximo
        self.numero_canais = numero_canais

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
    
    def volume_acima(self):
        if self.volume == self.volume_maximo:
            pass
        else:
            self.volume += 1

    def volume_abaixo(self):
        if self.volume == 0:
            pass
        else:
            self.volume -= 1

    def imprimir(self):
        return f"Ligado: {self.ligado}, canal sintonizado: {self.canal}, volume: {self.volume}, numero de canais: {self.numero_canais}, volume máximo: {self.volume_maximo}"

tv = Televisor(True, 15, 48, 50, 35)

print(tv.imprimir())
tv.volume_acima()
print(tv.imprimir())
tv.volume_acima()
print(tv.imprimir())
tv.volume_acima()

print(tv.imprimir())

print()

tv2 = Televisor(True, 18, 2, 50, 35)

print(tv2.imprimir())
tv2.volume_abaixo()
print(tv2.imprimir())
tv2.volume_abaixo()
print(tv2.imprimir())
tv2.volume_abaixo()

print(tv2.imprimir())