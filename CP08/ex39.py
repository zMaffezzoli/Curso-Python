global A
global B

A = 10
B = 20

def Troque(a, b):

    c = a
    A = b
    B = c

    return A, B


print(A, B)
print(Troque(A,B))