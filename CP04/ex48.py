total_segundos = 5405
horas = total_segundos//3600
minutos = (total_segundos - horas*3600)//60
segundos = (total_segundos - horas*3600) + (total_segundos - minutos*60) - total_segundos

print(f"{total_segundos} segundos é {horas}h {minutos}min {segundos}seg")