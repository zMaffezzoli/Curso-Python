class Televisor:
    def __init__(self):
        self.ligado = True
        self.canal = 12
        self.volume = 43

    def imprimir(self):
        return f"Ligado: {self.ligado}, canal sintonizado: {self.canal}, volume: {self.volume}"
    

tv = Televisor()
print(tv.imprimir())