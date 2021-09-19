def leiaint():
    while True:
        try:
            n = int(input('Digite Um Numero Inteiro: '))
            break
        except:
            print('\033[91mErro! Digite Um Número Inteiro Nálido.\033[m')
    return f'Você Digitou O Número Inteiro {n}'


def leiafloat():
    while True:
        try:
            n = float(input('Digite Um Numero Real: '))
            break
        except:
            print('\033[91mErro! Digite Um Número Inteiro Válido.\033[m')
    return f'Você Digitou O Número Real {n}'


print(f'{leiaint()}\n{leiafloat()}')
