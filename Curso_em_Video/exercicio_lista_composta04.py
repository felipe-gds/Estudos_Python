#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear
#6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
print("#"*50)
print("="*19, "MEGA SENA", "="*19)
print("#"*50)
qnt = int(input("Digite o número de jogos: "))
lista = []
jogos = []
cont2 = 0
while cont2 < qnt:
    cont = 0
    while cont < 6:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
        cont += 1
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    cont2 += 1
for x, y in enumerate(jogos):
    print(f'Jogo {x+1}: {y}')
    sleep(2)