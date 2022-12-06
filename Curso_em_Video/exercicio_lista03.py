## exercicio que ordena a lista sem utilizar " count ";
'''
num = list()
for c in range(0, 4):
    dig = int(input("Digite um valor: "))
    if c == 0 or dig > num[-1]:
        num.append(dig)
        print("Valor adicionado ao final da lista.")
    else:
        pos = 0
        while pos <= len(num):
            if dig <= num[pos]:
                num.insert(pos, dig)
                print(f'Valor adicionado na posição {pos}')
                break
            pos += 1
print(num)
'''
# A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
esc = 's'
num = list()
while esc in 'Ss':
    num.append(int(input("Digite um número: ")))
    esc = str(input("Deseja digitar mais um número? "))
print(f'Foram digitados {len(num)} números.')
num.sort(reverse=True)
print(f'Os números em ordem decrescente {num}')
if 5 in num:
    print("Foi digitado o número 5")
else:
    print('Não foi digitado o número 5')