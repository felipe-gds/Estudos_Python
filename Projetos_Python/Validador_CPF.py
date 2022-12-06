while True:
    cpf = input("Digite seu CPF(apenas números): ")
    novo_cpf = []
    cpf_validador = cpf[:9]
    mult = 10
    acumulador = 0
    acumulador2 = 0
    for n in cpf:
        novo_cpf.append(int(n)) if n.isdigit() else... ## transforma em int e lista
        continue
    del(novo_cpf[9:11])

    for cont in novo_cpf:
        result = cont * mult
        acumulador += result
        mult -= 1

    dig1 = 11 - (acumulador % 11)
    if dig1 > 9:
        dig = 0
    novo_cpf.append(dig1)
    mult = 12
    cpf_validador = cpf_validador + (str(dig1))
    for cont in novo_cpf:
        mult -= 1
        result = cont * mult
        acumulador2 += result

    dig2 = 11 - (acumulador2 % 11)
    cpf_validador = cpf_validador + (str(dig2))
    sequencia = cpf_validador == str(cpf_validador[0]) * 11  ## invalidar sequencia de numeros iguais

    msg = "CPF válido!" if cpf == cpf_validador and not sequencia else "CPF inválido"
    print(msg)


