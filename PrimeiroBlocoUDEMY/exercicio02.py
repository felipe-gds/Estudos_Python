##01Faça um programa que peça ao usuário para digitar um número inteiro,
##informe se este número é par ou ímpar. Caso o usuário não digite um número
##inteiro, informe que não é um número inteiro.

'''
num_1 = input('Digite um número inteiro ')

if num_1.isdigit():
    num_1 = int(num_1)

    if num_1 % 2 == 0:
      print(f'{num_1} é um número par')
    else:
      print(f'{num_1} é um número impar')

else:
    print('Não é um número inteiro ')
'''

##2Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
##descrito, exiba a saudação apropriada. Ex.
##Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""
horas = input('Que horas são? ')

if horas.isdigit():
    horas = int(horas)
    if horas <= 11:
        print('Bom dia!')
    elif horas <= 17:
        print('Boa tarde! ')
    elif horas <= 23:
        print('Boa noite! ')
    else:
        print('Não é uma hora válida')
else:
    print('Não é uma hora válida')
"""

##3Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
##menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
##"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".

nome = input("Digite seu nome ")
nome = len(nome)

if nome <= 4:
    print("Seu nome é curto")
elif nome <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é grande")



