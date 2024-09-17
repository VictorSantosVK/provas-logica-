multip5 = 0

while True:
    numero = int(input(""))
    if numero == 0:
        break

    if numero % 5 == 0:
        multip5 += numero
    
print(multip5)

    
#faça um programa que receba uma quantidade indeterminada de numeros inteiros positivos até que o usuário digite zero, calcule e exiba a soma daqueles numeros multiplos de 5:

#entrada: a entrada consiste em multiplas linhas contendo numeros inteiros positivos. A ultima linha do conjunto de valores será zero.

#saída: a saída consiste em um unico valor contendo a soma dos numeros multiplos de 5

#exemplo de entrada :
# 5
# 15
# 15
# 2
# 4
# 10
#0
#exemplo de saída 
#55
