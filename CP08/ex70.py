def reduz(a, b):
    return a / b

def neg(racional):
    return racional - (racional * 2)

def soma(racionalx, racionaly):
    return racionalx + racionaly

def mult(racionalx, racionaly):
    return racionalx * racionaly

def div(racionalx, racionaly):
    return racionalx / racionaly

racional1 = reduz(1, 2)
racional2 = reduz(3, 4)

print(racional1)
print(racional2)

print(neg(racional1))
print(neg(racional2))

print(soma(racional1, racional2))

print(mult(racional1, racional2))

print(div(racional2, racional1))