""""
palavras = 'ternura', 'amor', 'paixao', 'perdao', 'harmonia', 'resiliencia', 'empatia'
for c in palavras:
    print(f'\nNa palavra {c.upper()}, temos as vogais, ', end='') ## \n quebra de linha, end= mesma linha
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
"""
esc = "s"
num = []
while esc in 'sS':
    dig = int(input("Digite um número: "))
    if dig in num:
        print("Número repetido.")
        continue
    else:
        num.append(dig)
    esc = str(input("Deseja acrescentar mais números? [s/n]"))
print(sorted(num)) ## ordena a lista < ou num.sort() >