
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
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except():
        print('Houve um erro ao cadastrar nova pessoa ')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except():
            print('Houve um erro ao escrever novo dado ')
        else:
            print(f'Novo registro de {nome} cadastrado com sucesso ')
