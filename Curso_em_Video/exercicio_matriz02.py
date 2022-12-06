#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

soma_par = soma_terceira = maior = 0
matriz = [0, 0, 0], [0, 0, 0], [0, 0, 0]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor de {l, c}'))
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
        if matriz[1][c] >= maior:
            maior = matriz[1][c]
        if matriz[l][2]:
            soma_terceira += matriz[l][2]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end="")
    print()
print("A soma de todos os valores pares é: ", soma_par)
print("A soma dos valores da terceira coluna é: ", soma_terceira)
print("O maior valor da segunda linha é: ", maior)
