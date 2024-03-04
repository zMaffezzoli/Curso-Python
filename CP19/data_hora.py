import datetime

"""agora = datetime.datetime.now()
print(agora.replace(hour=22, minute=30))"""

nascimento = input("Informe sua data de nascimento (DD/MM/AAAA): ")
dd_mm_aa = nascimento.split('/')

date = datetime.datetime(year=int(dd_mm_aa[2]), month=int(dd_mm_aa[1]), day=int(dd_mm_aa[0]))
print(date)