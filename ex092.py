from datetime import date
pessoa = dict()
pessoa['nome'] = input('Nome: ')
nascimento = int(input('ano nascimento: '))
pessoa['ctps'] = int(input('CTPS (0 não tem): '))
anoatual = date.today().year

pessoa['idade'] = anoatual - nascimento

if pessoa['ctps'] != 0:
    pessoa['ano contratação'] = int(input('Ano de Contratação: '))
    pessoa['salario'] = float(input('Salario: R$'))
    apos = pessoa['ano contratação'] + 35
    pessoa['idade aposentadoria'] = apos - nascimento
print(15*'-=')
for k, v in pessoa.items():
    print(f'- {k} = {v}')
