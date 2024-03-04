from equipamento import Equipamento
from computador import Computador

class TestaEquipamento:
    def __init__(self):
        pass

    def main(self):
        equipamento = Equipamento(30, 2015)
        equipamento.exibe()
        print()
        computador = Computador(4500, 2020, "Intel i5", "GTX 1050")
        computador.exibe()

testa_equipamento = TestaEquipamento()
testa_equipamento.main()