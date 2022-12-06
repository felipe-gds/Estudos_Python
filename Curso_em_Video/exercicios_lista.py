num = []
for n in range(0, 4):
    num.append(int(input(f'Digite um número na posição {n}: ')))

print(f'Você digitou os números {num}.')
print(f'O maior número foi o {max(num)}, na posição: ', end="")
for x, y in enumerate(num):
    if y == max(num):
        print(f'{x}...', end="")
