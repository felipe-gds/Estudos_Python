print(f'{"Loja do china":=^30}')
preco = float(input("Qual o valor? "))
pagamento = 0
while pagamento > 4 or pagamento < 1:
    pagamento = int(input("Digite a forma de pagamento: \n [1] No dinheiro; \n [2] Cartão; \n "
                          "[3] 2 x no cartão;\n [4] 3x no cartão.\n"))
    if pagamento == 1:
        break
    elif pagamento == 2:
        preco = preco + preco * 0.10
    elif pagamento == 3:
        preco = preco + preco * 0.15
    elif pagamento == 4:
        preco = preco + preco * 0.20
    else:
       print("Opção inexistente!")
print(f'Sua compra ficou no valor de R${preco}')





