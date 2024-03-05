def ler(habitante):
    
    for chave, valor in habitante.items():
        print(f"{chave}: {valor}")

def media_idade(habitantes):
    idades = 0

    for i in habitantes:
        idades += i["idade"]

    return idades / len(habitantes)

def maior_idade(habitantes):
    idades = []

    for i in habitantes:
        idades.append(i["idade"])

    return max(idades)

def caracteristica_especifica(habitantes):
    caracteristica = 0

    for i in habitantes:
        if i["sexo"] == "feminino" and i["idade"] >= 18 and i["idade"] <= 35 and i["cor_olhos"] == "A" and i["cor_cabelo"] >= "L":
            caracteristica += 1

    return caracteristica

habitante1 = {"sexo": "feminino", "cor_olhos": "A", "cor_cabelo": "P", "idade": 16}
habitante2 = {"sexo": "masculino", "cor_olhos": "C", "cor_cabelo": "L", "idade": 20}
habitante3 = {"sexo": "feminino", "cor_olhos": "A", "cor_cabelo": "L", "idade": 18}
habitante4 = {"sexo": "masculino", "cor_olhos": "A", "cor_cabelo": "P", "idade": 20}
habitante5 = {"sexo": "feminino", "cor_olhos": "P", "cor_cabelo": "P", "idade": 36}

habitantes = [habitante1, habitante2, habitante3, habitante4, habitante5]

ler(habitante1)
print(media_idade(habitantes))
print(maior_idade(habitantes))
print(caracteristica_especifica(habitantes))