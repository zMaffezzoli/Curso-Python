carlos = 3_000
joao = carlos / 3

meses = 0

while True:

    carlos *= 1.02
    joao *= 1.05

    meses += 1

    if joao >= carlos:
        print(f"Foram necessários {meses} meses para a poupança de João passar ou se igualar a de Carlos")
        break

    else:
        pass