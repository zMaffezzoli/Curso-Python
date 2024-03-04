from random import randint

a = str(randint(1, 9999))
b = str(randint(1, 9999))

print(a, b)

vetorstr_a = list(a)
vetorstr_b = list(b)

vetorint_a = []
vetorint_b = []

for i in vetorstr_a:
    vetorint_a.append(int(i))

for i in vetorstr_b:
    vetorint_b.append(int(i))

vetor_prontoa = [min(vetorint_a)]
vetor_prontob = [min(vetorint_b)]

vetorstr_a.remove(str(vetor_prontoa[0]))
vetorstr_b.remove(str(vetor_prontob[0]))

for i in vetorstr_a:
    vetor_prontoa.append(int(i))

for i in vetorstr_b:
    vetor_prontob.append(int(i))    

print(vetor_prontoa)
print(vetor_prontob)
print(f"Soma dos algatismos de a e b: {sum(vetor_prontoa) + sum(vetor_prontob)}")