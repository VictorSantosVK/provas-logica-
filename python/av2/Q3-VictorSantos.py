x = int (input())

def calcConta (consumo):
    vTotal = 7

    if consumo > 100:
        vTotal += (consumo - 100)*5
        consumo = 100

    if consumo > 30 :
        vTotal += (consumo -30)*2 
        consumo = 30

    if consumo > 10:
        vTotal += (consumo - 10)*1

    return vTotal

vConta = calcConta(x)
print(vConta)