def media(nota1, nota2, nota3, tipo_media="A"):
    notas = [nota1, nota2, nota3]

    if tipo_media == "A":
        return sum(notas) / len(notas)
    
    elif tipo_media == "P":
        return ((nota1 * 5 + nota2 * 3 + nota3 * 2) / 10)
    
    else:
        return "Operação não existe"
    
print(media(5, 7, 10))
print(media(5, 7, 10, "P"))
print(media(5, 7, 10, "C"))