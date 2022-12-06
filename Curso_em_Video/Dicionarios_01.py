alunos = dict()
alunos['nome'] = str(input('Digite o nome do aluno: '))
alunos['nota'] = int(input('Digite a nota: '))
if alunos['nota'] >= 7:
    alunos['situacao'] = 'Aprovado'
else:
    alunos['situacao'] = 'Reprovado'
for k, v in alunos.items():
    print(f'{k} => {v}.')

