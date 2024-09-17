def encontrar_campea(arquivo_entrada, arquivo_saida):
    campea = ""
    mSalto = -1 

    with open(arquivo_entrada, 'r') as file:
        for linha in file:
            dados = linha.split() 
            nome = dados[0] 
            saltos = list(map(float, dados[1:]))  
           
            mSaltoAtual = max(saltos)
           
            if mSaltoAtual > mSalto:
                mSalto = mSaltoAtual
                campea = nome

    # Escrever o nome da campeã no arquivo de saída
    with open(arquivo_saida, 'w') as file:
        file.write(campea)
        
encontrar_campea('saltos.dat', 'campea.dat')