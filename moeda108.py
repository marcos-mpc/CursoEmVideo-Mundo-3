def formatacao(n=0):
    return f'R${n:.2f}'.replace('.', ',')


def aumentar(n=0, p=0):
    res = n + (n * (p / 100))
    return res


def diminuir(n=0, p=0):
    res = n - (n * (p / 100))
    return res


def dobro(n=0):
    res = n * 2
    return res


def metade(n=0):
    res = n / 2
    return res
