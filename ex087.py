print(20*'*')
print('EXAMINANDO MATRIZ')
print(20*'*')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
cont = cont1 = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            cont += matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if c == 2:
            cont1 += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma de todos os valores pares é igual à: {cont}')
print(f'A soma dos valores da terceira coluna é igual à {cont1}')
print(f'O maior valor da linha 2 é {max(matriz[1])}')
