import datetime

"""ano_novo = datetime.datetime(2025, 1, 1, 0)
agora = datetime.datetime.now()

print(f"Falta {ano_novo - agora} para o ano novo")"""

agora = datetime.datetime.now()
vencimento_boleto = agora + datetime.timedelta(days=3)

print(vencimento_boleto)