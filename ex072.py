print(10*'-=')
print('NUMEROS POR EXTENSO')
print(10*'-=')
numeros = ('ZERO', 'UM', 'DOIS', 'TRES', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE',
           'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
n = int(input('Escolha um numero de 0 a 20: '))
while n > 20:
    n = int(input('TENTE NOVAMENTE! Escolha um numero de 0 a 20: '))
print(f'vc escolheu o numero {numeros[n]}!')
