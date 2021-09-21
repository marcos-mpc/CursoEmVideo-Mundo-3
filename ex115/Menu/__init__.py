from adicionais import cor, linha


def menu():
    while True:
        try:
            print(linha())
            print(f'{"MENU PRINCIPAL":^40}')
            print(linha())
            print(f'{cor(3)}1 -{cor(0)} {cor(4)}Ver pessoas cadastradas')
            print(f'{cor(3)}2 -{cor(0)} {cor(4)}Cadastrar nova pessoa')
            print(f'{cor(3)}3 -{cor(0)} {cor(4)}mSair do sistema{cor(0)}')
            print(linha())
            n = int(input(f'{cor(3)}Sua opção:{cor(0)} '))

        except(TypeError, ValueError):
            print(f'{cor(1)}Erro! Digite um número inteiro válido.{cor(0)}')
        else:
            if n > 3 or n < 1:
                print(f'{cor(1)}Erro! Digite um número válido.{cor(0)}')
            if n == 3:
                break
            elif n == 2:
                print(linha())
                print(f'{cor(7)}{"Opção 2":^40}{cor(0)}')
                print(linha())
            elif n == 1:
                print(linha())
                print(f'{cor(7)}{"Opção 1":^40}{cor(0)}')
    return 'Saindo do sistema... volte sempre.'


print(menu())