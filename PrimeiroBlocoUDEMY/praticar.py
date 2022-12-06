"""
while True:
    num = input("Digite um número ")

    if not num.isnumeric():
         print("Digite apenas números ")
         continue

    num = int(num)
    a = num - 1
    s = num + 1

    print("O antecessor de {} é {} e o sucessor é {}".format(num, a, s))
    break
"""
'''
num = int(input("Digite um número "))
raiz = num ** (1/2)
print(f"O dobro de {num} é {num * 2}")
print(f"A raiz de {num} é {raiz}")
'''
while True:
    nota1 = input('Primeira Nota ')
    nota2 = input('Segunda Nota ')
    nota3 = input('Terceira Nota ')

    caracteres1 = len(nota1)
    caracteres2 = len(nota2)
    caracteres3 = len(nota3)

    if caracteres1 > 2:
        print("Nota invalida ")
    elif caracteres2 > 2:
        print("Nota invalida ")
    elif caracteres3 > 2:
        print("Nota invalida ")
    else:
        break

nota1 = int(nota1)
nota2 = int(nota2)
nota3 = int(nota3)
media = (nota1 + nota2 + nota3) / 3
print(f"A sua média é {media:.2f}")





