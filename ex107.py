import moeda

n = float(input('Digite um valor: '))
print(f'A metade de {n} é igual à {moeda.metade(n)}')
print(f'O dobro de {n} é igual à {moeda.dobro(n)}')
print(f'Com aumento de 10% fica {moeda.aumentar(n, 10)}')
print(f'Com redução de 13% fica {moeda.diminuir(n, 13)}')
