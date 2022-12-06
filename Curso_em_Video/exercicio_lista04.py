#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
#conter apenas os valores pares e os valores ímpares digitados, respectivamente.
'''
lista = []
esc = 's'
while esc in 'sS':
    lista.append(int(input("Escreva um número: ")))
    esc = str(input('Deseja continuar?:[s/n] '))
print(f'Digitados {lista}')
pares = []
impar = []
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impar.append(c)
print(f'Pares {pares}')
print(f'Ímpares {impar}')
'''

#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
#deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
lista = []
pilha = []
exp = str(input('Digite uma expressão.'))
for c in exp:
    lista.append(c)
    if c == '(':
        pilha.append(c)
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(c)
if len(pilha) == 0:
    print("Expressão correta!")
else:
    print("Expressão incorreta.")