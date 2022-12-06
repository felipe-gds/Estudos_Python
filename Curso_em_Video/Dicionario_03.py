#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
cadastro = dict()
cadastro['nome'] = str(input("Digite o nome: "))
cadastro['nascimento'] = int(input("Ano de nascimento: "))
cadastro['idade'] = datetime.now().year-cadastro['nascimento']              # utiliza a data do pc
cadastro['carteira'] = int(input('Número carteira de trabalho (0 não tem)'))
if cadastro['carteira'] != 0:
    cadastro['contratação'] = int(input("Ano de contratação. "))
    cadastro['aposentadoria'] = 35 + cadastro['idade'] - (datetime.now().year-cadastro['contratação'])
    if cadastro['aposentadoria'] > 65:
        cadastro['aposentadoria'] = 65
    cadastro['salario'] = float(input("Qual o salário: "))
for k, v in cadastro.items():
    print(f'-- {k} --- {v}')

