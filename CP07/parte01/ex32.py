vetor_x = [1, 2, 3, 4, 6]
vetor_y = [6, 7, 8, 9, 10]

for i in range(len(vetor_x)):
    print(f"Soma de cada elemento de x e y: {vetor_x[i] + vetor_y[i]}")

for i in range(len(vetor_x)):
    print(f"Produto de cada elemento de x e y: {vetor_x[i] * vetor_y[i]}")

print(f"Elementos de x que não existam em y: {set(vetor_x).difference(set(vetor_y))}")

print(f"Elementos que existam em ambos: {set(vetor_x).intersection(set(vetor_y))}")

print(f"Todos os elementos de x, e todos os elementos y que não estão em x: {set(vetor_x).union(set(vetor_y))}")