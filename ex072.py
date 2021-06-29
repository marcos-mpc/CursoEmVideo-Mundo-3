print(10*'-=')
print('NUMEROS POR EXTENSO')
print(10*'-=')
numeros = ('ZERO', 'UM', 'DOIS', 'TRES', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE',
           'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    n = int(input('Escolha um numero de 0 a 20: '))
    while n > 20 or n < 0:
        n = int(input('TENTE NOVAMENTE! Escolha um numero de 0 a 20: '))
    print(f'vc escolheu o numero {numeros[n]}!')
    eslha = input('deseja continuar ? [S/N] ').strip().upper()[0]
    if eslha == 'N':
        break
