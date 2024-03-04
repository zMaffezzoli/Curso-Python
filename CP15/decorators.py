"""
São funções que decoram outras funções (aprimoram outras funções)
"""

def seja_educado(funcao):
    def sendo():
        print("Foi um prazer conhecer você!")
        funcao()
        print("Até mais!")

    return sendo

@seja_educado           # Mesma coisa --> seja_educado(apresentacao)
def apresentacao():     # A função decorada recebe as mesmas funcionalidades da sua Function Decorator
    print("Meu nome é Douglas")

apresentacao()

print()

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f"O primeiro argumento deve ser {valor}"
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento("pizza") # Passa um valor para a Function decorator
def comida_favorita(*args):
    print(args)


print(comida_favorita("pizza", "picanha"))
print(comida_favorita("picanha", "pizza")) # Retorna a validação