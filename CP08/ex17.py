def soma_entre_numeros(inicial, final):
    total = 0

    for i in range(inicial+1, final):
        total += i

    return total

print(soma_entre_numeros(1, 5))
print(soma_entre_numeros(5, 10))
print(soma_entre_numeros(10, 15))