def leiaint(txt):
    num = 0
    while True:
        nu = str(input(txt))
        if nu.isnumeric():
            num = int(nu)
            break
        else:
            print('Erro! Digite um numero!')
    return num


n = leiaint('Digite um Numero: ')
print(f'Você digitou o numero {n}')
