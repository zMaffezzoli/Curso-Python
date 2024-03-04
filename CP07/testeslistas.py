# ALguns metodos de listas
"""
Pop()    Exclui o ultimo elemento da lista e/ou o indice desejado
extend() insere elemento interaveis ao final da lista([1,2,3,4] / "String")
append()  insere um elemento no final da lista
insert()  insere um elemento informando seu indice
clear()  limpa uma lista
copy()  copia uma lista sem alterar a lista copiada (diferente de nova = lista)
index() acha indice do elemento desejado
"""

lista = [1, 2, 3]

n1, n2, n3 = lista # n1 = 1, n2 = 2, n3 = 3

lista.append(4)

lista.extend("Abacate")
lista.extend([5, 6, 7])


lista.insert(1, "B")
print(lista)

# lista = list(range(1, 11))
# lista = list("Abacate")

lista_palavra = ["Nada", "como", "programar", "em", "Python"]
palavra = ' '.join(lista_palavra)
print(palavra)

palavra2 = "Sei lá"

print(palavra2.split(' '))