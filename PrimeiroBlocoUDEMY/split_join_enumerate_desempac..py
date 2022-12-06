'''
split = dividir uma string
join = juntar uma lista #str
enumerate = enumerar elementos da lista # interaveis
'''

frase = "Tu que te tornas eternamente responsável, por aquilo que cativas"

lista = frase.split(" ")
lista2 = frase.split(", ")
##print(lista)
##print(lista2)

##for valor in lista:
##    print(valor, "---", lista.count(valor))

##for c in enumerate(lista):
##    print(c)

"""
DESEMPACOTAMENTO DE LISTAS
"""

lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v1, v2, v3, * resto = lista3
print(resto)

### exercicios guanabara (palimdromo)
frase = str(input('Digite uma frase.')).upper()
frase1 = frase.split()
junto = "".join(frase1)                       ##ou usa a função . replace(" ", "") resumiria tudo!
invertido = ''
for c in range(len(junto) -1, -1, -1):        ## uma forma mais simples  for c in junto(::-1):
    invertido += junto[c]
print(invertido)
if junto == invertido:
    print("É um palimdromo")
else:
    print("Não é um palimdromo")