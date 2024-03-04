class Televisao:
    def __init__(self):
        self.__volume = 10
        self.__canal = 1

    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, volume):
        self.__volume = volume
    
    @property
    def canal(self):
        return self.__canal
    
    @canal.setter
    def canal(self, canal):
        self.__canal = canal

class ControleRemoto:
    def __init__(self):
        pass

    def aumenta_volume(self, televisao):
        if televisao.volume == 100:
            return f"Volume está no máximo"
        
        televisao.volume += 1
        return f"Volume: {televisao.volume}"
    
    def diminui_volume(self, televisao):
        if televisao.volume == 0:
            return f"Volume está no mudo"
        
        televisao.volume -= 1
        return f"Volume: {televisao.volume}"

    def diminui_canal(self, televisao):
        if televisao.canal == 1:
            return f"Não há canais abaixo de 0"
        
        televisao.canal -= 1
        return f"canal: {televisao.canal}"

    def aumenta_canal(self, televisao):
        televisao.canal += 1
        return f"canal: {televisao.canal}"

    def canal_especifico(self, televisao, canal):
        if canal >= 1:
            televisao.canal = canal
            return f"canal: {televisao.canal}"
        
        return f"Não há canais abaixo de 0"
        

televisao = Televisao()
controle = ControleRemoto()

print(controle.aumenta_volume(televisao))
print(controle.aumenta_volume(televisao))
print()
print(controle.diminui_volume(televisao))
print(controle.diminui_volume(televisao))
print()
print(controle.diminui_canal(televisao))
print(controle.aumenta_canal(televisao))
print(controle.aumenta_canal(televisao))
print(controle.diminui_canal(televisao))
print()
print(controle.canal_especifico(televisao, 558))
print(controle.diminui_canal(televisao))