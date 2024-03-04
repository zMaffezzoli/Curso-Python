"""
- Sets não possuem valores duplicados
- Sets não possuem valores ordenados 
- Não são acessados via indice
- Não possui ordenação
"""

s = {1, 2, 3, 4, 5, 6, 6, 7, 7}

print(s)

s.add(8)

print(s)

s.discard(1) # Ou remove() // discard não gera erro caso não encontrar o valor no set

print(s)

s1 = {1,2,3,4,5}

s2 = {5,6,7,8,4}

unico_set = s1.union(s2) # Ou s1 | s2 União entre dois sets

ambos = s1.intersection(s2) # Ou s1 & s2 Valor em ambas

print(ambos)

so_s1 = s1.difference(s2) # Valores que estão em s1, mas não em s2
print(so_s1)