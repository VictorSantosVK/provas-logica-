X = int(input())

def fatorialDuplo (X):
    if X % 2 == 0:
        return "O número deve ser ímpar e positivo"
    
    resultado = 1
    
    for x in range(1, X+1 ,2): #iterand apenas sobre os numeros impares
        resultado *= x
    return resultado
    

print(fatorialDuplo(X))