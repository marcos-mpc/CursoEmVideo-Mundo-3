print(f'{20*"="}\n{"SITUAÇÃO DE ALUNOS"}\n{20*"="}')

aluno = {'nome': input('Nome: '), 'media': float(input('Média: '))}
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO!'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO!'
else:
    aluno['situação'] = 'REPROVADO!'
print(20*'-=')
for k, v in aluno.items():
    print(f' - {k} é igual à {v}')
