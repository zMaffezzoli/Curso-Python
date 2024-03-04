chegada = input('Digite a hora da chegada (12 50): ')
partida = input('Digite a hora da partida (16 50): ')

hora_chegada = int(chegada[:2]) * 60 + int(chegada[3:])

hora_partida = int(partida[:2]) * 60 + int(partida[3:])

if hora_partida > hora_chegada:

    quantidade_horas = (hora_partida - hora_chegada) / 60

    if quantidade_horas > 0 and quantidade_horas <= 1:
        print(f"Deverá pagar R$1,00")

    elif quantidade_horas > 1 and quantidade_horas <= 2:
        print(f"Deverá pagar R$2,00")

    elif quantidade_horas > 2 and quantidade_horas <= 3:
        print(f"Deverá pagar R$4,20")

    elif quantidade_horas > 3 and quantidade_horas <= 4:
        print(f"Deverá pagar R$5,60")

    else:
        if not(quantidade_horas*60) % 60:
            print(f"Deverá pagar R${quantidade_horas*2}")

        else:
            quantidade_horas = int(quantidade_horas) + 1
            print(f"Você deverá pagar R${quantidade_horas*2}")

else:
    quantidade_horas = 24 - (hora_chegada - hora_partida) / 60
    
    if quantidade_horas > 0 and quantidade_horas <= 1:
        print(f"Deverá pagar R$1,00")

    elif quantidade_horas > 1 and quantidade_horas <= 2:
        print(f"Deverá pagar R$2,00")

    elif quantidade_horas > 2 and quantidade_horas <= 3:
        print(f"Deverá pagar R$4,20")

    elif quantidade_horas > 3 and quantidade_horas <= 4:
        print(f"Deverá pagar R$5,60")

    else:
        if not(quantidade_horas*60) % 60:
            print(f"Deverá pagar R${quantidade_horas*2}")

        else:
            quantidade_horas = int(quantidade_horas) + 1
            print(f"Você deverá pagar R${quantidade_horas*2}")