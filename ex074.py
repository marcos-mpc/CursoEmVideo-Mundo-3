from random import randint
print(22*'=')
print('MAIOR E MENOR DA TUPLA')
print(22*'=')
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = n[0]
menor = n[0]
for m in range(1, 5):
    if n[m] > maior:
        maior = n[m]
    if n[m] < menor:
        menor = n[m]
print(f'a lista gerada foi: {n}')
print(f'o maior numero foi: {maior}')
print(f'o menor numero foi: {menor}')
