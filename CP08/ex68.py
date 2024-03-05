def intercalada(string1, string2):
    lista = [len(string1), len(string2)]
    concatenacao = ""

    for i in range(min(lista)):
        concatenacao += string1[i] + string2[i]

    if len(string1) > len(string2):
        concatenacao += string1[len(string2) - len(string1):]

    elif len(string2) > len(string1):
        concatenacao += string2[len(string1) - len(string2):]
    
    string1 = concatenacao

    return string1

print(intercalada("banana", "ABACATEEE"))
print(intercalada("ABACATEEE", "banana"))