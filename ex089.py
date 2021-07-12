lista = list()
aluno = list()
notas = list()
cont = 0
while True:
    aluno.append(input('Nome do aluno: '))
    for n in range(0, 2):
        notas.append(float(input(f'digite a {n+1} nota do aluno: ')))
    aluno.append(notas[:])
    lista.append(aluno[:])
    notas.clear()
    aluno.clear()
    cont += 1
    print(20*'=')
    escl = input('Quer continuar ? [S/N] ')
    if escl in 'Nn':
        break

print('=' * 20)
print(f'{"Nº":<5}{"NOME":<10}{"MÉDIA"}')
for c in range(0, cont):
    print(f'{c:<5}', end='')
    print(f'{lista[c][0]:<10}', end='  ')
    print(f'{(lista[c][1][0] + lista[c][1][1]) / 2:}')

while True:
    print(30*'=')
    mostrar = int(input('deseja mostrar as notas de qual aluno ? (999 interrompe) '))
    print(30*'=')
    if mostrar == 999:
        break
    else:
        print(f'As notas de {lista[mostrar][0]} são {lista[mostrar][1]}')
print(22 * '=')
print('PROGRAMA INTERROMPIDO!')
