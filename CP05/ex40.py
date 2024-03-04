custo_fabrica = 25500

if custo_fabrica < 12000:
    total = custo_fabrica + custo_fabrica*0.05
    print(f"O custo que você terá será de: R${total}, sem impostos, somente com a comissãodo distribuidor")

elif custo_fabrica >= 12000 and custo_fabrica <= 25000:
    total = custo_fabrica + custo_fabrica*0.1 + custo_fabrica*0.15
    print(f"O custo que você terá será de: R${total}, com impostos e com a comissão do distribuidor")

else:
    total = custo_fabrica + custo_fabrica*0.15 + custo_fabrica*0.20
    print(f"O custo que você terá será de: R${total}, com impostos e com a comissão do distribuidor")