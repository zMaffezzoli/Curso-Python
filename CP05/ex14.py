trabalho_laboratorio = float(input("Digite uma nota: ")) 
avaliacao_semestral = float(input("Digite uma nota: ")) 
exame_final = float(input("Digite uma nota: ")) 

if trabalho_laboratorio < 0 or trabalho_laboratorio > 10 or avaliacao_semestral < 0 or avaliacao_semestral > 10 or exame_final < 0 or exame_final > 10:
    print("Notas inválida!")

else:
    media = (trabalho_laboratorio*2 + avaliacao_semestral*3 + exame_final*5) / 10
    
    if media <= 2.9:
        print('Reprovado')

    elif media >= 3 and media <= 4.9:
        print('Recuperação')

    else:
        print('Aprovado')
