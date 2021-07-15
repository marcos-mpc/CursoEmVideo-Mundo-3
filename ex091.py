from random import randint
from time import sleep
lista = list()
jogador = dict()
maior = 0
for n in range(0, 4):
    num = randint(1, 6)
    jogador[f'jogador{n+1}'] = num
    lista.append(jogador.copy())
    del jogador[f'jogador{n+1}']
for e, c in enumerate(lista):
    for j in c:
        print(f'{j} tirou {lista[e][j]}')
        sleep(1)
