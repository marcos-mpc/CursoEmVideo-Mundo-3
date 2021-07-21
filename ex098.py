print(f'{15*"*"}\n{"CONTADOR":^15}\n{15*"*"}')


def contador(i, f, p):
    if i > f:
        p = p - (p * 2)
    for c in range(i, f+1, p):
        print(c, end=' ')
    print()


contador(1, 10, 1)
contador(10, 0, 2)
contador(i=(int(input('inicio: '))),
         f=(int(input('fim: '))),
         p=(int(input('passo: '))))
