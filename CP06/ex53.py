andar = int(input("Digite quantos andares deseja exibir do triângulo de Floyd: "))

num = 1
for j in range(1, andar + 1):

    for i in range(1, j + 1):
        print(num, end=" ")
        num += 1
        
    print()