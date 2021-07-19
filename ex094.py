print(f'{30*"-="}\n{"CADASTRO E ANALEZE DE PESSOAS":^60}\n{30*"-="}')
lista = list()
pessoa = dict()
soma = 0
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = input('Resposta invalida! Digite M ou F: ').strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    opc = input('Continuar ? [S/N] ')
    lista.append(pessoa.copy())
    while opc not in 'SsNn':
        opc = input('Resposta invalida! Digite S ou N: ')
    if opc in 'Nn':
        break
print(30*'-=')
print(f'A) Foram cadastradas {len(lista)} pessoas.')
print(f'B) A média de idade do grupo é {soma / len(lista):.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')
for c in lista:
    if c['sexo'] == 'F':
        print(c['nome'], end=' ')
print()
print('Lista de pessoas que estão acima da media de idade do grupo:')
for i in lista:
    if i['idade'] > soma / len(lista):
        print(f'Nome = {i["nome"]}, Sexo = {i["sexo"]}, Idade = {i["idade"]}')
print(30*'-=')
