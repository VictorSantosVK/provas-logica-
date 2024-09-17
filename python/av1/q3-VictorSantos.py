# Leitura da entrada
preco_atual = float(input(""))
venda_media_mensal = int(input(""))

# Cálculo do novo preço
if venda_media_mensal < 500 or preco_atual < 30:
    novo_preco = preco_atual * 1.10 
elif 500 <= venda_media_mensal < 1200 or 30 <= preco_atual <= 80:
    novo_preco = preco_atual *+ 1.15
elif venda_media_mensal > 1200 or preco_atual > 80:
    novo_preco = preco_atual *- 1.20
else:
    novo_preco = preco_atual

# Saída do novo preço
print(f"{novo_preco:.2f}")
