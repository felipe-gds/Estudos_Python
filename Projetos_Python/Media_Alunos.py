contador = 1
maior = 0
media = 0
melhor = 'n'
print(f"{'':#^20}")
qnt = int(input("Quantos alunos? "))
while contador <= qnt:

    print(f"{'':#^20}")
    nome = input(f"Qual o nome do aluno {contador}?")
    contador = contador + 1
    nota = float(input("Qual sua nota? "))
    if nota > maior:
        maior = nota
        melhor = nome
    media = media + nota

media = media / qnt

print(f"O melhor aluno foi {melhor} com nota {maior}!")
print(f"E a média da turma foi de {media}")