entrada = input("")
resposta = entrada .split()

def cInvestigado (resposta):
    rPositiva = resposta.count('S')
    
    if rPositiva == 2:
        return "suspeitO"
    
    elif 3 <= rPositiva <= 4:
        return "Cumplice"
    
    elif rPositiva == 5:
        "Assassino"

    else:
        return "inocente"
    
resultado = cInvestigado (resposta)
print(resultado)
