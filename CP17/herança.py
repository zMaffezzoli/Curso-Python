class A:
    def __init__(self, a):
        self.a = a

class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

classe_b = B("a", "b")

print(classe_b.a)
print(classe_b.b)