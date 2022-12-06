galera = list()
dados = list()
for c in range(0, 3):
        dados.append(str(input("Digite um nome: ")))
        dados.append(int(input("Digite a idade: ")))
        galera.append(dados[:]) # a importancia do simbolo [:] para fazer uma cópia, não alterando original.
        dados.clear()
for x in galera:
    print(f'idades {x[1]}')  # printar elementos em um indice da lista

    if x[1] >= 18:
        print(x[0], "é maior.")
    else:
        print(x[0], "é menor.")