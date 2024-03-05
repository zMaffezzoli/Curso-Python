from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "agenda.txt")

mes = "03"

try:
    arquivo = open(arquivotxt, mode='a+', encoding="UTF-32")
    while True:

        print(f"a) inserir contato \nb) remover contato \nc) pesquisar contato pelo nome \nd) listar todos os contatos \ne) listar contatos cujo nome inicia com uma letra \nf) imprimir aniversariantes do mês \ng) sair")
        opcao = input("Digite a opção desejada: ")


        if opcao == "a":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            aniversario = input("Digite o aniversário do contato (DD/MM): ")

            arquivo.write(f"{nome} - {telefone} - {aniversario}\n")

        elif opcao == "b":
            arquivo.seek(0)
            linhas = arquivo.readlines()
            arquivo.close()

            nome = input("Digite o nome do contato que deseja remover: ")
            
            for i in range(len(linhas)):
                if nome in linhas[i]:
                    linhas.pop(i)

            arquivo = open(arquivotxt, mode='w', encoding="UTF-32")

            for i in range(len(linhas)):
                arquivo.write(linhas[i])

        elif opcao == "c":
            arquivo.seek(0)
            linhas = arquivo.readlines()

            nome = input("Digite o nome do contato que deseja buscar: ")
        
            for i in linhas:
                if nome in i:
                    print(i)
        
        elif opcao == "d":
            arquivo.seek(0)
            linhas = arquivo.readlines()
        
            for i in linhas:
                print(i)

        elif opcao == "e":
            arquivo.seek(0)
            linhas = arquivo.readlines()

            letra = input("Digite a letra que deseja buscar os contatos: ")

            for i in linhas:
                if i[0].upper() == letra.upper():
                    print(i)

        elif opcao == "f":
            arquivo.seek(0)
            linhas = arquivo.readlines()

            for i in linhas:
                if i[i.index("/") + 1 : -1] == mes:
                    print(i)

        else:
            arquivo.close()
            break

except Exception as err:
    print(f"Não foi possível criar o arquivo, erro: {err}")