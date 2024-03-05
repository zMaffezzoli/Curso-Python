from math import pi

def volume_esfera(raio):
    return f"Volume da esfera de raio {raio}: {(4/3) * pi * (raio**3)}"

print(volume_esfera(5))
print(volume_esfera(10))