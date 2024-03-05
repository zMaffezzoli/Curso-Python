def dentroRet(v1, v2, ponto):

    ponto_inferior_direito = (v2[0], v1[1])
    ponto_superior_esquerdo = (v1[0], v2[1])
    
    if ponto[0] >= v1[0] and ponto[0] <= v2[0] and ponto[1] >= v1[1] and ponto[1] <= v2[1]:
        return 1
    
    return 0


ponto1 = (5, 12)
ponto2 = (4, 14)
ponto3 = (6, 16)
v1 = (5, 7)  # ponto inferior esquerdo
v2 = (10, 15) # ponto superior direito

print(dentroRet(v1,v2,ponto1))
print(dentroRet(v1,v2,ponto2))
print(dentroRet(v1,v2,ponto3))