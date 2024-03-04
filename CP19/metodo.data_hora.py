import datetime

# Adiciona dois dias a data atual e deixa no horário 00
manutencao_sistema = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=2), datetime.time())
print(manutencao_sistema)

agora = datetime.datetime.today()

print(agora.strftime('%d/%m/%Y')) # Formatado em pt-BR