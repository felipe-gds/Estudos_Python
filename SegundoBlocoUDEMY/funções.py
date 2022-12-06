##1
'''
def soma(x, y, z):
    c = x + y + z
    print(c)

a = 50
b = 80
c = 46
soma(a, b, c) ## ou soma(50, 80, 46)

##2
def saudacao(m1, m2):
    print(m1, m2, "!")

nome = input("Qual seu nome?")
saudacao("olá", nome)

##3
def porcentagem(valor, porcent):
    final = valor + (valor / 100 * porcent)
    return final

prod = int(input("Qual o valor?"))
taxa = int(input("Qual a porcentagem da taxa?"))
print(porcentagem(prod, taxa))
'''

##4
def fizzbuzz (numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return f"FizzBuzz {numero}"
    if numero % 3 == 0:
        return f"Fizz {numero}"
    if numero % 5 == 0:
        return f"Buzz {numero}"
    return (numero)
##dig = int(input("Digite um número: "))
##print(fizzbuzz(dig))

from random import randint
for c in range(100):
     aleatorio = randint(0, 100)
     print(fizzbuzz(aleatorio))





