from datetime import date
print(f'{20*"-"}\n{"VOTAÇÃO":^20}\n{20*"-"}')


def voto(ano):
    print(30*'-')
    idade = date.today().year - ano
    print(f'Com {idade} anos, ', end='')
    if idade >= 70 or 16 <= idade <= 17:
        return opcoes[1]
    elif idade < 16:
        return opcoes[2]
    else:
        return opcoes[0]


opcoes = ('O VOTO É OBRIGATÓRIO!', 'O VOTO É OPCIONAL!', 'O VOTO É NEGADO!')
votacao = voto(int(input('Em que ano você nasceu ? ')))
print(votacao)
