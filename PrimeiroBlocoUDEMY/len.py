"""
Contagem de caracteres "len"
"""
"""
string1 = input("Digite seu cpf ")

caracterescpf = len(string1)

if caracterescpf < 11:
    print("Falta caracteres ")
elif caracterescpf > 11:
    print("Muitos caracteres ")
else:
    print("Analizando CPF")
"""
while True:
  CPF = input("Digite seu CPF: ")
  Qnt_carac = len(CPF)

  if Qnt_carac > 11 or Qnt_carac < 11:
    print("CPF invalido")
  else:
    print("analisando")