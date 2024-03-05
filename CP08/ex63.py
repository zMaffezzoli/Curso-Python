def compara(string1, string2):
    if string1 == string2:
        return f"São iguais"
    
    return f"São diferentes"

print(compara("abacaxi", "abacaxi"))
print(compara("abacaxi", "Abacaxi"))