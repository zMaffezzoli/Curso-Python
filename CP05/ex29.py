from random import randint

acertos = 0

for i in range(5):
    a = randint(1,100)
    b = randint(1,100)

    pergunta = int(input(f'Qual é a soma de {a} + {b}? '))

    if pergunta == a + b:
        acertos += 1

    else:
        pass

print(f"Você acertou {acertos}/5")