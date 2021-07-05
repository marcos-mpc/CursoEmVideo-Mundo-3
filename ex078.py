print(30*'=')
print(f'{"maior e menor de uma lista":^30}')
print(30*'=')
lista = []
for c in range(0, 5):
    lista.append(int(input(f'digite um valor na posição {c}: ')))
print(50*'=')
print(f'o maior valor digitado foi {max(lista)}, e está nas posições ', end='')
for e, i in enumerate(lista):
    if i == max(lista):
        print(f'{e}', end='...')
print(f'\no menor valor digitado foi {min(lista)}, e está nas posições ', end='')
for e, f in enumerate(lista):
    if f == min(lista):
        print(f'{e}...', end='')
print()
print('='*50)
