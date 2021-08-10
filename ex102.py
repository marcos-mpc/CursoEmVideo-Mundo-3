def fatorial(a, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param a: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta
    :return: o valor do Fatorial de um n.
    """
    n = a
    f = 1
    while n > 0:
        if show:
            print(f'{n}', ' x ' if n > 1 else ' = ', end='')
        f *= n
        n -= 1
    return f


print(fatorial(5, True))
