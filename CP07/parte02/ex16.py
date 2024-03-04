aluno1 = {"Matricula": 132, "Q1": "A", "Q2": "E","Q3": "B","Q4": "A","Q5": "E","Q6": "A", "Q7": "E","Q8": "C", "Q9" :"A", "Q10": "B", "nota": 0}
aluno2 = {"Matricula": 545, "Q1": "A","Q2": "E","Q3": "B","Q4": "E","Q5": "E","Q6": "D","Q7": "B","Q8": "C", "Q9": "D", "Q10": "E", "nota": 0}
aluno3 = {"Matricula": 623, "Q1": "A", "Q2": "E","Q3": "E", "Q4": "A", "Q5": "D", "Q6": "A", "Q7": "D", "Q8": "C", "Q9": "A", "Q10": "B", "nota": 0}

gabarito = {"Q1": "A", "Q2": "E","Q3": "B","Q4": "C","Q5": "E","Q6": "A", "Q7": "E","Q8": "C", "Q9" :"A", "Q10": "B"}

for chave, valor in gabarito.items():
    
    if valor == aluno1[chave]:
        aluno1["nota"] += 1

    if valor == aluno2[chave]:
        aluno2["nota"] += 1

    if valor == aluno3[chave]:
        aluno3["nota"] += 1

percentual = (aluno1["nota"] + aluno2["nota"] + aluno3["nota"]) / 3

print(f"Matrícula: {aluno1['Matricula']}, Respostas: {aluno1['Q1']}, {aluno1['Q2']}, {aluno1['Q3']}, {aluno1['Q4']}, {aluno1['Q5']}, {aluno1['Q6']}, {aluno1['Q7']}, {aluno1['Q8']}, {aluno1['Q9']}, {aluno1['Q10']}, Nota: {aluno1['nota']}")
print(f"Matrícula: {aluno2['Matricula']}, Respostas: {aluno2['Q1']}, {aluno2['Q2']}, {aluno2['Q3']}, {aluno2['Q4']}, {aluno2['Q5']}, {aluno2['Q6']}, {aluno2['Q7']}, {aluno2['Q8']}, {aluno2['Q9']}, {aluno2['Q10']}, Nota: {aluno2['nota']}")
print(f"Matrícula: {aluno3['Matricula']}, Respostas: {aluno3['Q1']}, {aluno3['Q2']}, {aluno3['Q3']}, {aluno3['Q4']}, {aluno3['Q5']}, {aluno3['Q6']}, {aluno3['Q7']}, {aluno3['Q8']}, {aluno3['Q9']}, {aluno3['Q10']}, Nota: {aluno3['nota']}")

print(f"Percentual de aprovação: {percentual}")