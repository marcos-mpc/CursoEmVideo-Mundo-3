from random import randint
from time import sleep


def maior (*num):
    print(30*'-=')
    print('Analisando valores...')
    for c in num:
        print(f'{c}', end=' ', flush=True)
        sleep(0.5)
    print(f'foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}')


maior(randint(0, 10), randint(0, 10), randint(0, 10),
      randint(0, 10), randint(0, 10), randint(0, 10))

maior(randint(0, 10), randint(0, 10), randint(0, 10))

maior(randint(0, 10), randint(0, 10))

maior(randint(0, 10))

maior(0)
