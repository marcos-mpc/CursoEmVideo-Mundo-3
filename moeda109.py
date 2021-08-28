def formatacao(n=0):
    return f'R${n:.2f}'.replace('.', ',')


def aumentar(n=0, p=0, f=False):
    res = n + (n * (p / 100))
    if f is True:
        return formatacao(int(res))
    else:
        return res


def diminuir(n=0, p=0, f=False):
    res = n - (n * (p / 100))
    if f is True:
        return formatacao(int(res))
    else:
        return res


# Resultado Curso

def dobro(n=0, f=False):
    res = n * 2
    return res if f is False else formatacao(res)


def metade(n=0, f=False):
    res = n / 2
    return res if not f else formatacao(res)
