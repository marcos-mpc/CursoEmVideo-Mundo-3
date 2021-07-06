print(25*'=')
print('LISTA COM VALORES UNICOS')
print(25*'=')

lista = []
while True:
    num = int(input('digite um numero: '))
    if num not in lista:
        lista.append(num)
        print('adicionado...')
    else:
        print('número ja existente!')
    esc = input('deseja continuar ? S/N ').strip().upper()[0]
    if esc == 'N':
        break
print(f'a lista digitada foi {sorted(lista)}')
