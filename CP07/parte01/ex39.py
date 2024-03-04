from math import factorial

linhas = int(input("Digite quantas linhas deseja ver: "))

for i in range(linhas): 
    
    for j in range(i+1): 
        print(factorial(i) // (factorial(j)*factorial(i-j)), end=" ") 
  
    
    print()