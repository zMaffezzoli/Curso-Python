class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

class Agenda:
    def __init__(self):
        self.__agenda = []

    def armazena_pessoa(self, pessoa):
        if len(self.__agenda) < 10:
            self.__agenda.append(pessoa)
            return f"Pessoa adicionada!"
        
        else:
            return f"Agenda cheia!"
        
    def remove_pessoa(self, nome_pessoa):
        for i in range(len(self.__agenda)):
            if self.__agenda[i].nome == nome_pessoa:
                self.__agenda.pop(i)
                return f"Pessoa removida da agenda!"
        
        else:
            return f"Está pessoa não está na lista!"
        
    def busca_pessoa(self, nome_pessoa):
        for i in range(len(self.__agenda)):
            if self.__agenda[i].nome == nome_pessoa:
                return f"A pessoa está na posição {i + 1}"
        else:
            return f"A pessoa não está na lista"
            
    def imprime_agenda(self):
        if len(self.__agenda) != 0:
            for i in self.__agenda:
                print(f"Nome: {i.nome}, idade: {i.idade}, altura: {i.altura}")

        else:
            return f"Lista vazia!"
    
    def imprime_pessoa(self, index):
        return f"Nome: {self.__agenda[index - 1].nome}, idade: {self.__agenda[index - 1].idade}, altura: {self.__agenda[index - 1].altura}"
    


agenda = Agenda()
pessoa1 = Pessoa("Bernardo", 20, 1.80)
pessoa2 = Pessoa("Alice", 15, 1.55)
pessoa3 = Pessoa("Luciano", 20, 1.70)
pessoa4 = Pessoa("Anderson", 17, 1.75)

print(agenda.armazena_pessoa(pessoa1))
print(agenda.armazena_pessoa(pessoa2))
print(agenda.armazena_pessoa(pessoa3))
print(agenda.armazena_pessoa(pessoa4))

print()

agenda.imprime_agenda()
print(agenda.busca_pessoa("Luciano"))

print()

print(agenda.imprime_pessoa(2))

print()

print(agenda.remove_pessoa("Alice"))

print()
agenda.imprime_agenda()
print(agenda.busca_pessoa("Alice"))