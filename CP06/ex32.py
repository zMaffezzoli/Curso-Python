from random import randint

lancar = ""

while lancar == "":
    lancar = input("Para rolar aperte enter, para parar aperte qualquer tecla e enter: ")

    dado1 = randint(1, 6)
    dado2 = randint(1, 6)

    print(f"Dado1: {dado1} / Dado2: {dado2}\n")

    if dado1 > dado2:
        print(f"Dado1 > Dado2")

    elif dado2 > dado1:
        print(f"Dado2 > Dado1")

    else:
        print(f"Dado1 = Dado2")