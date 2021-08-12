def ajuda(txt):
    from time import sleep
    print(f'\033[42m{35*"*"}\n{"ACESSANDO BIBLIOTECA/FUÇÕES":^35}\n{35*"*"}')
    sleep(1)
    print('\033[40;7m', end='')
    help(txt)
    sleep(1)


while True:
    print('\033[m', end='')
    print(f'\033[44m{35*"*"}\n{"SISTEMA DE AJUDA PyHELP":^35}\n{35*"*"}')
    f = input('\033[mFunções/Biblioteca =>')
    if f.upper() == 'FIM':
        print(f'\033[41m{35*"*"}\n{"Fim do programa!":^35}\n{35*"*"}')
        break
    else:
        ajuda(f.lower())
