import moeda109

n = float(input('Digite um valor: '))
print(f'A metade de {moeda109.formatacao(n)} é igual à {moeda109.metade(n, True)}')
print(f'O dobro de {moeda109.formatacao(n)} é igual à {moeda109.dobro(n, True)}')
print(f'Com aumento de 10% fica {moeda109.aumentar(n, 10, True)}')
print(f'Com redução de 13% fica {moeda109.diminuir(n, 13, True)}')
