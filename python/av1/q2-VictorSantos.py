# Entrada do usuário
ninicial = int(input())
nfinal = int(input())

# Inicializando a soma
soma = 0

# Iterando pelos números entre ninicial e nfinal, excluindo nfinal
for num in range(ninicial, nfinal):
    soma += 3 * num

# Exibindo o resultado
print(soma)