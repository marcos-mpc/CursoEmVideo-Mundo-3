def formatacao(n=0):
    return f'R${n:.2f}'.replace('.', ',')


def aumentar(n=0, p=0, f=False):
    res = n + (n * (p / 100))
    return res if not f else formatacao(res)


def diminuir(n=0, p=0, f=False):
    res = n - (n * (p / 100))
    return res if not f else formatacao(res)


def dobro(n=0, f=False):
    res = n * 2
    return res if not f else formatacao(res)


def metade(n=0, f=False):
    res = n / 2
    return res if not f else formatacao(res)


def resumo(numero=0, aumento=10, reducao=5):
    print(f'{30*"-"}\n{"RESUMO DO VALOR":^30}\n{30*"-"}')
    tabela = {'Preço Analizado:': formatacao(numero), 'Dobro Do Preço:': dobro(numero, True),
              'Metade Do Preço:': metade(numero, True), f'{aumento}% De Aumento:': aumentar(numero, aumento, True),
              f'{reducao}% De Redução:': diminuir(numero, reducao, True)}
    for k, v in tabela.items():
        print(f'{k:<20}{v}')
    print(30*'-')
