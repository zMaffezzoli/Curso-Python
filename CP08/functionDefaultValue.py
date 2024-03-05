def exponencia(numero=2, potencia=2): # Cria um valor padrão para um parâmetro caso o mesmo não seja passado
    """Função para calcular exponencia de números"""  # Cria uma documentação para meu elemento | teste c/ help(exponencia())
    
    return numero ** potencia

print(exponencia())           # Daria erro, porém foi criado um valor padrão para o parâmetro
print(exponencia(potencia=3)) #Atribui valor somente a potencia, numero continua default

print(exponencia(5,3)) 


total = 5
def teste():  # Podemos utilizar a mesma variavel do escopo global com global total
    total = 0 
    total += 1
    print(total)

teste()
print(total)