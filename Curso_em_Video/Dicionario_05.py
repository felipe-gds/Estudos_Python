'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
lista = list()
mulheres = list()
dados = dict()
resp = "s"
soma = 0
while resp in "Ss":
    dados['nome'] = str(input("Digite o nome: "))
    while True:
        dados['sexo'] = str(input("Digite o sexo [M/F]: "))
        if dados['sexo'] in "fF" or dados['sexo'] in "mM":
            break
        print("ERRO! Digite um sexo válido!")
    dados['idade'] = int(input("Digite a idade: "))
    soma += dados['idade']
    resp = str(input("Deseja cadastrar outro usuário?[s/n] "))
    lista.append(dados.copy())
print("=-"*20)
print(f'Pessoas cadastradas: {len(lista)}.')
media = soma / len(lista)
print(f'Média: {media:.2f}')
print("Mulheres: ")
for c in lista:
    if c['sexo'] in "fF":
        print(f' {c["nome"]}', end=' - ')
print('')
print("Pessoas com idade acima da média: ")
for c in lista:
    if c['idade'] > media:
        print(f'{c["nome"]}', end=' - ')