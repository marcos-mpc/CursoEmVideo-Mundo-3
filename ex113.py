def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
            break
        except(ValueError, TypeError):
            print('\033[91mErro! Digite Um Número Inteiro Nálido.\033[m')
    return f'Você Digitou O Número Inteiro {n}'


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
            break
        except():
            print('\033[91mErro! Digite Um Número Inteiro Válido.\033[m')
    return f'Você Digitou O Número Real {n}'


print(f'{leiaint("Digite Um Número Inteiro: ")}\n{leiafloat("Digite Um Numero Real: ")}')
