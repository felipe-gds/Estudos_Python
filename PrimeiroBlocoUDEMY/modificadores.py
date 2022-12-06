"""
Formatando valores com modificadores

:s - strings
:d - inteiros
:f - float
:.(numeros)f - qnt de casas decimais ex. :.2f
:(caracteres)< , >, ou ^ (quantidade) (tipo - s, d ou f)

< direita
> esquerda
^ centro
"""
'''
nome = input("digite seu nome ")
formatar = (f"{nome:#^50}")
print(formatar)
'''
'''
num_1 = int(input('Digite um número '))
num_2 = int(input('Digite outro número '))

divisao = num_1 / num_2
print(f"{divisao:.3f}")
'''
""""
nome = input("Digite seu nome: ")
print(f"{nome:-^''}")
"""

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
divisao = (num1 / num2)
print(f"{divisao:.3f}")




