numero = int(input("Digite um valor: "))
desolver = 0

if numero > 0:
    for i in str(numero):
        desolver += int(i)
    print(desolver)
    
else:
    print("Número inválido")