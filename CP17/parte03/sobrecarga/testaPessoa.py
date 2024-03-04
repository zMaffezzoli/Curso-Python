from pessoa import Pessoa

class TestaPessoa:
    def __init__(self):
        pessoa1 = Pessoa("001", "Anderson", 10)
        # pessoa1.exibe
        pessoa1.exibe(1)
        print()
        pessoa1.exibe(0)
        
    def __init__(self, codigo, nome, idade):
        pessoa2 = Pessoa(codigo, nome, idade)
        # pessoa2.exibe()
        pessoa2.exibe(1)

testapessoa = TestaPessoa("002", "Julio", 18)