#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
#e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
futebol = dict()
jogos = []
total = 0
futebol['Nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input('Quantas partidas jogadas: '))
for c in range(partidas):
    jogos.append(int(input(f'Gols da {c+1}ª partida: ')))
futebol['Gols'] = jogos[:]
futebol['Total'] = sum(jogos)           ## Função que soma os números da lista
print("=-"*20)
for x, y in futebol.items():
    print(f'{x:<15} ==== {y}')
print("=-"*20)
print(f'O jogador {futebol["Nome"]}, jogou {partidas} partidas:')
for x, y in enumerate(jogos):
    print(f'Partida {x+1} conquistou {y} Gols.')



    
