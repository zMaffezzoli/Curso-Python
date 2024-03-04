premio = 15000

# O que cada um investiu
amigo1 = 100
amigo2 = 200
amigo3 = 300

#Soma do que cada um investiu
total = (amigo1+amigo2+amigo3)*100

#Atribuindo a % que cada um contribuiu a % do premio total
ganho_amigo1 = (amigo1*100/total) * premio
ganho_amigo2 = (amigo2*100/total) * premio
ganho_amigo3 = (amigo3*100/total) * premio

print(f"Investimentos: R${amigo1}, R${amigo2}, R${amigo3} \nValor do prêmio: R${premio} \nQuanto cada um ganharia: R${ganho_amigo1}, R${ganho_amigo2}, R${ganho_amigo3}")