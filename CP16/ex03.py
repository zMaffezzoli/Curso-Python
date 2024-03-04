class Elevador:
    def __init__(self, andares, capacidade):
        self.__andar_atual = 0
        self.__pessoas_elevador = []
        self.__andares = andares
        self.__capacidade = capacidade

    @property
    def andar_atual(self):
        return self.__andar_atual
    
    @andar_atual.setter
    def andar_atual(self, andar_atual):
        self.__andar_atual = andar_atual

    @property
    def pessoas_elevador(self):
        return self.__pessoas_elevador
    
    @pessoas_elevador.setter
    def pessoas_elevador(self, pessoas_elevador):
        self.__pessoas_elevador = pessoas_elevador

    @property
    def andares(self):
        return self.__andares
    
    @andares.setter
    def andares(self, andares):
        self.__andares = andares

    @property
    def capacidade(self):
        return self.__capacidade
    
    @capacidade.setter
    def capacidade(self, capacidade):
        self.__capacidade = capacidade

    def entra(self, pessoa):
        if len(self.__pessoas_elevador) < self.__capacidade:
            self.__pessoas_elevador.append(pessoa)
            return f"{pessoa} entrou no elevador"
        
        return f"{pessoa} não entrou no elevador, está cheio"
    
    def sai(self, pessoa):
        if len(self.__pessoas_elevador) != 0 and (pessoa in self.__pessoas_elevador):
            self.__pessoas_elevador.remove(pessoa)
            return f"{pessoa} saiu do elevador"

        elif len(self.__pessoas_elevador) == 0:
            return f"O elevador está vazio!"
            
        return f"{pessoa} não está no elevador"
    
    def sobe(self):
        if self.__andar_atual < self.__andares:
            self.__andar_atual += 1
            return f"Subiu para o andar {self.__andar_atual}"
        
        return f"O elevador já está no último andar"
    
    def desce(self):
        if self.__andar_atual > 0:
            self.__andar_atual -= 1
            return f"Desceu para o andar {self.__andar_atual}"
        
        return f"O elevador já está no térreo"
        
elevador = Elevador(5, 5)


print(elevador.sai("Jorge")) # não tem ninguém!
print(elevador.andar_atual) # 0
print(elevador.desce()) # Térreo
print()
print(elevador.sobe()) # 1
print(elevador.sobe()) # 2
print(elevador.sobe()) # 3
print()
print(elevador.desce()) # 2
print()
print(elevador.sobe()) # 3
print(elevador.sobe()) # 4
print(elevador.sobe()) # 5
print(elevador.sobe()) # Não sobre
print()
print(elevador.entra("Jorge"))
print(elevador.entra("Bruna"))
print(elevador.entra("Paulo"))
print(elevador.entra("Matheus"))
print(elevador.entra("Renan"))
print(elevador.entra("Lucas")) # Está cheio
print()
print(elevador.sai("Mateus")) # Não está no elevador
print(elevador.sai("Matheus")) # Matheus sai
print()
print(elevador.entra("Lucas")) # Pode entrar