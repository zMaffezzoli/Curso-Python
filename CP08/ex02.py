def data_texto(dia, mes, ano):
    match mes:
        case 1:
            return f"{dia} de janeiro de {ano}"
        
        case 2:
            return f"{dia} de fevereiro de {ano}"
        
        case 3:
            return f"{dia} de março de {ano}"
       
        case 4:
            return f"{dia} de abril de {ano}"
        
        case 5:
            return f"{dia} de maio de {ano}"
        
        case 6:
            return f"{dia} de junho de {ano}"
       
        case 7:
            return f"{dia} de julho de {ano}"
       
        case 8:
            return f"{dia} de agosto de {ano}"
        
        case 9:
            return f"{dia} de setembro de {ano}"
        
        case 10:
            return f"{dia} de outubro de {ano}"
        
        case 11:
            return f"{dia} de novembro de {ano}"
        
        case 12:
            return f"{dia} de dezembro de {ano}"
        
        case _:
            return f"Mês inválido"
        

print(data_texto(1,12,2005))