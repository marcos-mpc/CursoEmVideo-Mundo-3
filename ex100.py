from random import randint
from time import sleep
print(f'{20*"="}\n{"SORTEIO DE NUMEROS"}\n{20*"="}')
lista = list()


def sorteio(* num):
    print(30*'=')
    print('Sorteando 5 valores ', end='')
    for c in num:
        print(f'{c}', end=' ')
        sleep(0.3)
        lista.append(c)
    print()


def somapar(txt):
    print(30*'=')
    soma = 0
    for c in range(0, 5):
        if txt[c] % 2 == 0:
            soma += txt[c]
    print(f'A soma de todos os numeros par da lista {txt} foi {soma}')


sorteio(randint(0, 10), randint(0, 10), randint(0, 10),
        randint(0, 10), randint(0, 10))

somapar(lista)
