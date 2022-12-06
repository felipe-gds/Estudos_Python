##Aprimore o desafio 04 para que ele funcione com vários jogadores,
##incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

futebol = dict()
jogos = []
jogadores = []
total = 0
id = 0
while True:
    futebol.clear()
    jogos.clear()
    futebol['ID'] = id
    futebol['Nome'] = str(input('Digite o nome do jogador: '))
    partidas = int(input('Quantas partidas jogadas: '))
    for c in range(partidas):
        jogos.append(int(input(f'Gols da {c+1}ª partida: ')))
    futebol['Gols'] = jogos[:]
    futebol['Total'] = sum(jogos)           ## Função que soma os números da lista
    jogadores.append(futebol.copy())
    id += 1
    while True:
        resp = str(input("Quer continuar? [s/n]")).upper()[0]
        if resp == "N":
            break

print("=-"*22)
print('ID ==  Nome  === Gols === Total')
print("=-"*22)
for i in jogadores:
    for d in i.values():
        print(f'{str(d):<10}', end=" ")
    print("")
while True:
    mostrar = int(input("Mostrar dados de jogadores? (999 encerra)"))
    if mostrar == 999:
        break
    for x in jogadores:
        if x["ID"] == mostrar:
            print(f'Jogador {x["Nome"]} fez {x["Total"]} Gols: {x["Gols"]}')
print("ENCERRADO SISTEMA")