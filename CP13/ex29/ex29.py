from os import path

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "registros.txt")

try:
    arquivo =  open(arquivotxt, mode="w+", encoding="UTF-8")
    while True:
                print(f"\na) Incluir registro \nb) Excluir registro \nc) Alterar valor da venda \nd) Imprimir os registros \ne) sair")

                opcao = input("Digite a opção desejada: ")

                if opcao == "a":
                    cod_vendedor = input("Digite o código do vendedor: ")
                    nome_vendedor = input("Digite o nome do vendedor: ")
                    valor_venda = input("Digite o valor da venda: ")
                    mes = input("Digite o mes da venda(MM): ")

                    arquivo.seek(0)
                    linhas = arquivo.readlines()

                    if linhas == []:
                        arquivo.write(f"{cod_vendedor} - {nome_vendedor} / {valor_venda} | {mes}\n")  
                    
                    else:
                        for i in range(len(linhas)):
                            if linhas[i][0: (linhas[i].index("-") -1)] == cod_vendedor and linhas[i][(linhas[i].index("|") + 2): -1] == mes:
                                print("Já existe um registro com esse vendedor neste mesmo mês!")
                                break

                        else:
                            arquivo.write(f"{cod_vendedor} - {nome_vendedor} / {valor_venda} | {mes}\n")

                elif opcao == "b":
                    arquivo.seek(0)
                    linhas = arquivo.readlines()
                    arquivo.close()

                    cod_vendedor = input("Digite o código do vendedor: ")
                    mes = input("Digite o mes da venda(MM) que deseja excluir: ")

                    for i in range(len(linhas)):
                        if linhas[i][0: (linhas[i].index("-") -1)] == cod_vendedor and linhas[i][(linhas[i].index("|") + 2): -1] == mes:
                            linhas.pop(i)
                            break

                    arquivo = open(arquivotxt, mode='w+', encoding="UTF-8")

                    for i in range(len(linhas)):
                        arquivo.write(linhas[i])

                elif opcao == "c":
                    arquivo.seek(0)
                    linhas = arquivo.readlines()
                    arquivo.close()

                    cod_vendedor = input("Digite o código do vendedor: ")
                    mes = input("Digite o mes da venda(MM) que deseja excluir: ")
                    valor_venda = input("Qual será o valor da venda: ")

                    for i in range(len(linhas)):
                        if linhas[i][0: (linhas[i].index("-") -1)] == cod_vendedor and linhas[i][(linhas[i].index("|") + 2): -1] == mes:
                            antes = linhas[i][0: (linhas[i].index("/") + 1)]
                            depois = linhas[i][(linhas[i].index("|")): -1]
                            linhas.pop(i)

                            linhas.append(f"{antes} {valor_venda} {depois}")
                            break

                    arquivo = open(arquivotxt, mode='w+', encoding="UTF-8")

                    for i in range(len(linhas)):
                        arquivo.write(linhas[i])

                elif opcao == "d":
                    arquivo.seek(0)
                    linhas = arquivo.readlines()

                    for i in linhas:
                        print(i[:-1])
                
                else:
                    arquivo.close()
                    break

except Exception as err:
    print(f"Não foi possível criar o arquivo, erro: {err}")
