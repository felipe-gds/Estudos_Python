'''
produtos = []
fim = "s"
item = ""
while fim == "s":
    item = input("Digite o nome do item: ")
    produtos.append(item)
    fim = input("Deseja acrescentar mais um item? [s] ou [n] ")
    while fim != "s" and fim != "n":
         fim = input("Digite 's' ou 'n'")
print(produtos)
'''
