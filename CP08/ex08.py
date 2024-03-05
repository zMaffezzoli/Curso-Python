from math import sqrt

def hipotenusa(a=4, b=5):
    a **= 2
    b **= 2
    return sqrt(a + b)


print(hipotenusa())
print(hipotenusa(3, 4))