## Tuplas
produtos = 'Sandália', 5.99, 'Sapato', 7.50, 'Brusinha', 10, 'Melisinha', 7, 'legging', 9.90

print(f'{"Listagem de preços":^40}') ## alinhado ao centro
print("="*40)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}',end='') ## alinhado a esquerda
    else:
        print(f'R${produtos[c]:>7.2f}') ## alinhado a direita com 2 casas depois do zero
