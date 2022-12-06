#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
#sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
rodadas = dict()
classificacao = []
rodadas['jogador1'] = randint(0, 6)
rodadas['jogador2'] = randint(0, 6)
rodadas['jogador3'] = randint(0, 6)
rodadas['jogador4'] = randint(0, 6)
for k, v in rodadas.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)    # 1 segundo para aparecer o resultado
classificacao = sorted(rodadas.items(), key=itemgetter(1), reverse=True) #Organiza em ordem. itemgetter(1)
print("=-"*10)                                                           #selecionando o indice 1 do dicionario.
print("Classificação!")                                                  # E foram guardadas em uma lista.
for c, k in enumerate(classificacao):
    print(f'{c+1}º lugar o {k[0]} com {k[1]} pontos.')