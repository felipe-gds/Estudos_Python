"""
Operadores Relacionais
 ==   >    >=    <    <=    !=
"""

idade = int(input('Qual sua idade? '))

idade_min = 18
idade_max = 25
idade_proib = 23

if idade >= idade_min and idade <= idade_max and idade != idade_proib:
    print("Autorizado")
else:
    print('Não autorizado')
