def horas_segundos(horas=0, minutos=0, segundos=0):

    horas *= 3600
    minutos *= 60

    return horas + minutos + segundos

print(horas_segundos(1, 30))
print(horas_segundos(1))