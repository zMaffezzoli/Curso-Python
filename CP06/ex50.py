chico = 1.50
ze = 1.10

ano = 0

while True:
    chico += 0.02
    ze += 0.03

    ano += 1

    if ze > chico:
        print(f"Foram necessários {ano} anos para que Zé seja maior que Chico")
        break
    else:
        pass




while ze <= chico:
    chico += 0.02
    ze += 0.03
    ano += 1
print(f"Foram necessários {ano} anos para que Zé seja maior que Chico")
