nome = 'Felipe'
idade = 29
peso = 64
altura = 1.75
imc = idade / altura ** 2
ano_nasc = 2020 - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}')
print(f"{nome} nasceu em {ano_nasc}")
