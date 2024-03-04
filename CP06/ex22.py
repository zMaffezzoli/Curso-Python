media = 0 
qtd_notas = 0

while True:
    valor = float(input("Digite uma nota: "))

    if valor < 10 or valor > 20:
        break
    
    else:
        media += valor
        qtd_notas += 1

print(f"Média {media/qtd_notas}")