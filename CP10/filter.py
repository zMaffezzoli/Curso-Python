import statistics # Biblioteca para tratar com estatísticas

valores = [1, 2, 3, 4, 5, 6]

media = statistics.mean(valores) # Calcula média dos valores

filtro = list(filter(lambda x: x > media, valores)) # Filtra os valores que estão acima da média

print(filtro) # Assim como o map, os valores também se perdem após serem utilizados

paises = ["", "Brasil", "", "Argentina" , "Japão", ""]

#vazio = list(filter(None, paises)) # Retira dados vazios

vazio = list(filter(lambda pais: pais != "", paises)) # Mesma coisa, porém de forma mais explícita
print(vazio)