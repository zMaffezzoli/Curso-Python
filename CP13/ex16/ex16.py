from os import path
from random import randint

caminho = path.dirname(path.abspath(__file__))
arquivotxt = path.join(caminho, "numeros.txt")

try:
    numeros = [randint(1, 10000) for i in range(10)]
    
    with open(arquivotxt, mode="w", encoding="UTF-8") as arquivo:
        
        for i in numeros:
            binario = bin(i).replace("b", "0")
            arquivo.write(f"{i} = {binario}\n")

except Exception as err:
    print(f"Não foi possível criar um arquivo e escrever-lo, erro: {err}")