import moeda107

n = float(input('Digite um valor: '))
print(f'A metade de {n} é igual à R${moeda107.metade(n)}')
print(f'O dobro de {n} é igual à R${moeda107.dobro(n)}')
print(f'Com aumento de 10% fica R${moeda107.aumentar(n, 10)}')
print(f'Com redução de 13% fica R${moeda107.diminuir(n, 13)}')
