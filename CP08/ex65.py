def concatena(string1, string2, numero):
    string2 = string2[0:numero]
    concatenacao = string1
    string1 = None

    for i in string2:
        concatenacao += i

    return concatenacao

print(concatena("banana", "banana", 3))
print(concatena("abacaxi", "caxi", 4))