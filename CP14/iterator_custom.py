class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration
    

# Cria um próprio objeto iterable, ou seja, interável
# Exemplos de iterável: [Lists], "Strings", (Tuples)
# o iterator retorna por partes o iterable

# Exemplo na prática de iterator e iterable

"""for i in "palavra": # Palavra = iterable
    print(i)"""        # i = iterator

for i in Contador(1, 31):
    print(i)