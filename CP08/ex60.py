def substring(palavra, substring):
    if substring in palavra:
        return palavra.index(substring) + 1

    return -1

palavra = "abacaxi"
sub = "a"

palavra2 = "paralelepipedo"
sub2 = "le"

print(f"Substring '{sub}' está na posição: {substring(palavra, sub)} da palavra {palavra}")
print(f"Substring '{sub2}' está na posição: {substring(palavra2, sub2)} da palavra {palavra2}")