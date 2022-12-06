"""
       For___in____:
interando string com laço for
função RANGE(start, stop, step) ex. [ range(10, 100, 2) ]
"""

nome = "felipe guedes"
nome_novo = " "

for letra in nome:
    if letra == "f":
        nome_novo = nome_novo + letra.upper()
    elif letra == "g":
        nome_novo = nome_novo + letra.upper()
    else:
        nome_novo = nome_novo + letra
print(nome_novo)





"""
for n in range(100):
    if n % 8 == 0:
      print(n)
"""
