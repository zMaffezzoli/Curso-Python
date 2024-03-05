from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "alunos.txt")

class Cadastro_Aluno:
    def __init__(self):
        self.lista_alunos = []

    def cadastra_aluno(self, aluno):
        self.lista_alunos.append(aluno)

    def adiciona(self):
        arquivo = open(arquivotxt, mode="w", encoding="UTF-8")

        for i in self.lista_alunos:
            arquivo.write(i[0])

        arquivo.close()

try:
    cadastro = Cadastro_Aluno()

    qtd_alunos = int(input("Quantos alunos serão adicionados: "))

    for i in range(qtd_alunos):
        matricula = input("Digite a matricula do aluno: ")
        sobrenome = input("Digite um sobrenome do aluno: ")
        ano_nascimento = input("Digite o ano de nascimento: ")
        cadastro.cadastra_aluno([matricula + " " + sobrenome + " " + ano_nascimento + "\n"])

    cadastro.adiciona()

except Exception as err:
    print(f"Não foi possível criar o arquivo, erro: {err}")