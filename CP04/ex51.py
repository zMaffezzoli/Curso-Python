from math import sqrt

origem = (0, 0) #A
coordenada = (15, 30) #B

distancia = sqrt((coordenada[0] - origem[0])**2 + (coordenada[1] - origem[1])**2)

print(f"A distância da coordenada para origem é de : {distancia}")