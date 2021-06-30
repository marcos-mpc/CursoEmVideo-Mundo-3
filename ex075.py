n = (int(input('digite um numero: ')), int(input('digite mais um numero: ')),
     int(input('digite outro numero: ')), int(input('digite o ultimo numero: ')))
print(f'os valores degitados foram {n}')
print(f'o numero 9 aparece {n.count(9)}')
if 3 in n:
    print(f'o numero 3 aparece na {n.index(3) + 1}ª posição')
else:
    print('não foi digitado nenhum numero 3')
print('valor par digitado foi: ', end='')
for num in n:
    cont = 0
    if num % 2 == 0:
        print(f'{num}', end=' ')
