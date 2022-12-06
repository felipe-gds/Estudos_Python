"""
Listas em python
fatiamento
append: insere um valor no final da lista;
insert: insere um valor no meio da lista;
pop: deletar um elemento do final da lista;
del: deletar um elemento no meio da lista;
clear: apaga tudo ou uma fatia
extend: juntar duas listas
+
max: maior valor da lista
min: menor valor da lista
range: 
"""

lista = ["macaco", "cabra", "peixe"]
print(lista)
lista.append("avestruz")
print(lista)
lista.insert(1, "baleia")
print(lista)
lista.pop(2)  # ou del(lista[2])
print(lista)

secreta = "banana"
digitados = []
chances = 3

while (chances > 0):
    letra = input("Digite uma letra ")
    if len(letra) > 1:
        print("Digite apenas uma letra ")
        continue
    if letra in secreta:
        print(f'Palavra secreta contém a letra "{letra}"')
        digitados.append(letra)
    else:
        print(f'Ops, não existe a letra "{letra}"')
        chances = chances - 1
        print(f'Voce tem "{chances}"chances!')
        continue
    print_palavra = ""
    for letra_secreta in secreta:
        if letra_secreta in digitados:
            print_palavra += letra_secreta
        else:
            print_palavra += "*"
    print(print_palavra)
    if print_palavra == secreta:
      print("Parabéns!!!")
      break


## TUPLAS
#1
times = 'Palmeiras', 'Corinthians', 'Flamengo', 'Havai', 'Chapecoense', 'Vasco'
print("Os 2 primeiros são", times[:2])
print("Os 2 últimos são", times[-2:])
print("Em ordem alfabética", sorted(times))
print("Chapecoense está ná posição", times.index("Chapecoense"))
#2
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)) ##gera valores na tupla
print("Os números sorteados foram, ", numeros)
print("O maior é", max(numeros))
print("O menor é", min(numeros))








