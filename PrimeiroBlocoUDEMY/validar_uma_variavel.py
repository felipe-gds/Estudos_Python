##Funções para validar uma variavel

import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)

num_1 = input('Digite um número ')
num_2 = input('Digite um número ')

if is_int(num_1) and is_int(num_2):
    num_1 = int(num_1)
    num_2 = int(num_2)

    print(num_1 + num_2)
elif is_float(num_1) and is_float(num_2):
    num_1 = float(num_1)
    num_2 = float(num_2)

    print(num_1 + num_2)
else:
    print("error")