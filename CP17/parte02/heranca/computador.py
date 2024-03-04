from equipamento import Equipamento

class Computador(Equipamento):
    def __init__(self, preco, ano_lancamento, processador, placa_video):
        super().__init__(preco, ano_lancamento)
        self.__processador = processador
        self.__placa_video = placa_video

    @property
    def processador(self):
        return self.__processador
    
    @property
    def placa_video(self):
        return self.__placa_video
    
    @processador.setter
    def processador(self, processador):
        self.__processador = processador

    @placa_video.setter
    def placa_video(self, placa_video):
        self.__placa_video = placa_video

    def exibe(self):
        print(self._Equipamento__preco)
        print(self._Equipamento__ano_lancamento)
        print(self.__processador)
        print(self.__placa_video)