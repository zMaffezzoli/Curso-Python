# all() retorna True se todos os elementos do iteravel são verdadeiros ou se é um iteravel vazio
# any() retorna True se qualquer elemento for verdadeiro, retorna false se o iteravel é vazio

valores = [1, 2, 3, 4, 5]
valores2 = [0, 1, 2, 3]

nomes = ["Camila", "Carol", "Cassio"]
nomes2 = ["Camila", "Carol", "Cassio", "Daniel"]
print(all(valores))
print(all(valores2)) # 0 é false, logo retornará false
print(all([]))

print(all([nome[0] == "C" for nome in nomes])) # Verifica se o indice 0 de cada nome começa com "C"
print(all([nome[0] == "C" for nome in nomes2])) # Retorna false, pois Daniel começam com "D"


print(any(nome[0] == "C" for nome in nomes2)) # Retorna True, pois pelo menos um elemento começa com "C", além de usar o generator em vez de lista