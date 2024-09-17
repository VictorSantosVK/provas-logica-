entrada = input("")
numeros = list(map(int, entrada.split()))

def multi3(numeros):
    posicao = [] 
    multiplos = [] 
    
    #verificando se são multiplos de 3
    for x, numero in enumerate(numeros):
        if numero % 3 == 0:
            posicao.append(x) 
            multiplos.append(numero) 
    
    return posicao, multiplos

posicoes, multiplos = multi3(numeros)
print(" ".join(map(str, posicoes)))
print(" ".join(map(str, multiplos)))

