def leiaint(txt):
    num = 0
    while True:
        n = str(input(txt))
        if n.isnumeric():
            num = int(n)
            break
        else:
            print('Erro! Digite um numero!')
    return num



n = leiaint('Digite um Numero: ')
print(f'Você digitou o numero {n}')
