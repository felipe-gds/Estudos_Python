#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
lista = list()
dados = list()
esc = 's'
maior =  menor = 0
while esc in 'Ss':
    dados.append(str(input("Digite o nome: ")))
    dados.append(float(input("Digite o peso ")))
    if len(lista) == 0:
        menor = maior = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    esc = str(input("Deseja continuar? [s/n]"))
print("Foram cadastradas", len(lista), " pessoas. ")
print(f'O maior peso foi de {maior}', end="")
for c in lista:
    if c[1] == maior:
        print(f'[{c[0]}] ', end="")
print()
print(f'E o menor peso foi de {menor}', end="")
for c in lista:
    if c[1] == menor:
        print(f'[{c[0]}] ', end="")



