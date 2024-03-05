def soma(a, b):
    if type(a) is str or type(b) is str:
        raise TypeError("Valores não são do tipo int") # Altera/cria a mensagem de erro no terminal
    
    return a + b


print(soma(5, 6))
print(soma(5, "6"))