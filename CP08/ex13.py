def operacao(numero1, numero2, simbolo="+"):
    if simbolo == "+":
        return numero1 + numero2
    
    elif simbolo == "-":
        return numero1 - numero2
    
    elif simbolo == "*":
        return numero1 * numero2
    
    elif simbolo == "/":
        return numero1 / numero2
    
    else:
        return "Operação inválida"
    

print(operacao(1, 5))
print(operacao(1, 5, "-"))
print(operacao(1, 5, "*"))
print(operacao(1, 5, "/"))