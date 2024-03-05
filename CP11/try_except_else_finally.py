"""try:
    numero = int(input("Digite um número: "))

except ValueError as err:
    print(f"Vcoê não digitou um valor correto e deu o seguinte erro: '{err}'")

else:       # Só é executado se não entrar em nenhum bloco de erro
    print(f"Você digitou {numero}")

finally:    # É executado independente se der erro ou não (É usado para algo que deve sempre ser executado, independente de erro ou sucesso)
    print("Chegamos até aqui, tenha orgulho!")
  """  

"""TRATAR OS ERROS SEMPRE NAS FUNÇÕES"""

def dividir(a, b):
    try:
        return int(a) / int(b)
    
    except ValueError:
        return f"Valor inválido"
    
    except ZeroDivisionError:
        return f"Não é possível dividir um valor por zero"
    
num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

print(dividir(num1, num2))