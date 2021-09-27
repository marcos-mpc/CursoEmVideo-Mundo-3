
def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except():
        print('Erro ao criar arquivo!')
    else:
        print(f'Arquivo {nome} Criado Com Sucesso!')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except():
        print('Erro ao ler arquivo!')
    else:
        print(f'{40*"-"}\n{"PESSOAS CADASTRADAS":^40}\n{40*"-"}')
        print(a.read())
