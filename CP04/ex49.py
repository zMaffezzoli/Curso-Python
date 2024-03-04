horario_inicio = "14:32:30"
duracao = 39633 #11h

horas = duracao//3600
minutos = (duracao - horas*3600)//60
segundos = (duracao - horas*3600) + (duracao - minutos*60) - duracao

segundos_termino = (int(horario_inicio[6:]) + segundos)
minutos_termino = (int(horario_inicio[3:5]) + minutos)
horas_termino = (int(horario_inicio[:2]) + horas)

if segundos_termino > 60:
    minutos_termino += 1
    segundos_termino -= 60

if minutos_termino > 60:
    horas_termino += 1
    minutos_termino -= 60

if horas_termino > 24:
    horas_termino -= 24

print(f"Horário término: {horas_termino}:{minutos_termino}:{segundos_termino}")