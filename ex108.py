import moeda108

n = float(input('Digite um valor: '))
print(f'A metade de {moeda108.formatacao(n)} é igual à {moeda108.formatacao(moeda108.metade(n))}')
print(f'O dobro de {moeda108.formatacao(n)} é igual à {moeda108.formatacao(moeda108.dobro(n))}')
print(f'Com aumento de 10% fica {moeda108.formatacao(moeda108.aumentar(n, 10))}')
print(f'Com redução de 13% fica {moeda108.formatacao(moeda108.diminuir(n, 13))}')
