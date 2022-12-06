nome = 'Felipe'
idade = 29
altura = 1.75
peso = 64
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print("{n} tem {i} anos de idade e seu imc é {im:.2f}".format(n=nome, i=idade, im=imc))