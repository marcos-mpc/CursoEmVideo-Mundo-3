print(30*'*')
print('LISTA COM PARES E IMPARES')
print(30*'*')

lista = [[], []]

for c in range(0, 7):
    num = int(input(f'digite o {c+1}º valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print(f'a lista de numeros pares é: {sorted(lista[0])}')
print(f'a lista de numeros impares é: {sorted(lista[1])}')
