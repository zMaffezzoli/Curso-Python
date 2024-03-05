"""
try:
    len(5)

except: # Captura qualquer tipo de erro (genérico)
    print("Ocorreu algum problema")"""

try:
    #len(10) # TypeError
    #funcao() # NameError
    print("Abacate"[11]) # IndexError

except TypeError as erra: # Captura erros apenas do tipo dele
    print(f"Deu TypeError: {erra}")

except NameError as errb:
    print(f"Deu NameError: {errb}")

except:
    print("Deu um erro diferente")