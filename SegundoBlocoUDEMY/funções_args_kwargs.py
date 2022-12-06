'''
def teste (*args):
   print(args)

lista = ['Alo', 'galera', 'de', 'cowboy!']
teste(*lista)           ## dessa forma ele desempacota a lista para a


def teste2 (*args, **kwargs): ## dessa forma pode ou não receber parametros nomeados (key word arguments)
   nome = kwargs.get("nome")
   print(nome)
   print(type(args))

lista = [1, 2]
teste2(*lista, nome="Felipe", idade=20)

variavel = "navio"

def func():
   global variavel   ##prática não aceitável de alterar uma variavel global
   variavel = "barco"

func()
print(variavel)
'''
variavel = "navio"
def func2(arg):    ## forma mais aceitável de manipular a variavel global
   arg = "barco"
   return(arg)
variavel2 = func2(variavel)
print(variavel2)

