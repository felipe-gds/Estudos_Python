'''
Estruturas de repetição - while
Realizar uma ação enquanto uma condição for verdadeira.

"continue" pula para o próximo laço
"break" finaliza o laço
'''
"""
x = 0
while x < 10:
    y = 0
    while y < 5:
        print(f'({x}, {y})')
        y += 1
    x += 1    ## x + x + 1
print('Acabou!')
"""

"""
while True:
    num_1 = input("Digite um número ")
    num_2 = input("Digite outro número ")
    operador = input("Digite um operador (Ou se quiser sair digite [s]) ")

    if not num_1.isnumeric() or not num_2.isnumeric():
        print("digite apenas números!")
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == "+":
        print(num_1 + num_2)
    elif operador == "-":
        print(num_1 - num_2)
    elif operador == "*":
        print(num_1 * num_2)
    elif operador == "/":
        print(num_1 /num_2)
    elif operador == "s":
        print("Até logo!")
        break
    else:
        print("Digite um  operador válido")
"""

## acumuladores e contadores usando while e else
""""
contador = 1
acumulador = 0
while contador <= 5:
    print(contador, acumulador)
    acumulador += acumulador + contador
    contador = contador + 1
else:  ## quando a condição no laço for false
    print("fim!")
"""












