#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em
#uma lista composta. No final, mostre um boletim contendo a média de cada um e
#permita que o usuário possa mostrar as notas de cada aluno individualmente.
print("-="*5, "LANÇAMENTO DE NOTAS", "-="*5)
qnt = int(input("Quantos alunos serão lançados? "))
print("-="*22)
c = 0
geral = list()
while c < qnt:
    nome = str(input("NOME: "))
    nota1 = float(input("Nota 01: "))
    nota2 = float(input("Nota 02: "))
    media = (nota1 + nota2) / 2
    geral.append([nome, nota1, nota2, media])
    print(geral)
    c += 1
for x, y in enumerate(geral):
    print(f'Aluno {x+1} {geral[x][0]:<10}: Média: {geral[x][3]}  ')
while True:
    resp = int(input("Quais notas deseja ver? ('999' encerra): "))
    resp -= 1
    if resp == 998:
       break
    elif resp >= qnt or resp == -1:
        print("OPS! Digite numeração válida.")
        continue
    print(f'Notas de {geral[resp][0]} foram: {geral[resp][1]:<10} e {geral[resp][2]:>8}.')
print("   Tchau!!")



