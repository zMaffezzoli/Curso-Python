class NomeDaClasse:

    atri_class = 1.10   # Atributo de classe, é um atributo em comum que todas as instâncias terão com o mesmo valor

    @classmethod        # Método de classe, é um método em comum que todas as instâncias terão, recebe como atributo, a propria classe
    def metodo(cls):
        return cls.atri_class

    def __init__(self, atri1, atri2):
        self.atri1 = atri1          # Atributos de instância, são únicos para cada instância
        self.atri2 = atri2

    def __metodo(self):             # Método de instância privado, ou seja, só existe dentro da classe
        pass

classe1 = NomeDaClasse("atri1", "atri2")

classe1.atri3 = "atri3" # Atributo dinâmico, adiciona um atributo extra somente a aquela instância (incomum)

print(classe1.atri_class)
print(classe1.atri1)
print(classe1.atri2)
print(classe1.atri3)

print(NomeDaClasse.atri_class) # Não precisa de instância para existir
print(NomeDaClasse.metodo())   # Não precisa de instância para existir