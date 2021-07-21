print(f'{20*"="}\n{"TEXTO FORMATADO":^20}\n{20*"="}')


def escreva(txt):
    print((len(txt)+4) * '~')
    print(f'  {txt}')
    print((len(txt)+4) * '~')


escreva('Olá, Mundo!')
escreva('Estudando Mundo Python!')
escreva(input('digite algo: '))
