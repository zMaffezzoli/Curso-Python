from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "emp.txt")

try:

    with open(arquivotxt, mode="w", encoding="UTF-8") as arquivo:

        for i in range(5):
            profissao = input("Digite o nome da profissão: ")
            tempo_servico = input("Digite o tempo de serviço (em anos): ")

            arquivo.write(f"{profissao} ")
            arquivo.write(f"{tempo_servico} anos \n")

except Exception as err:
    print(f"Não foi possível criar o arquivo, erro: {err}")