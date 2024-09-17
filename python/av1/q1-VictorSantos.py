# Entrada do usuário
operacao = int(input())
num1 = int(input())
num2 = int(input())

# Verificando qual operação realizar
if operacao == 1:
    descricao = "média"
    resultado = (num1 + num2) / 2
elif operacao == 2:
    descricao = "diferença"
    resultado = abs(num1 - num2)
elif operacao == 3:
    descricao = "produto"
    resultado = num1 * num2
elif operacao == 4:
    descricao = "divisão"
    if num2 != 0:
        resultado = num1 / num2
        
print(descricao)
print(f"{resultado:.2f}")
