print(20*'=')
print('LISTA PAR E IMPAR')
print(20*'=')
lista = []
par = []
impar = []
while True:
    num = int(input('digite um numero: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    if num % 2 == 1:
        impar.append(num)
    opc = input('continuar ? [S/N]').strip().upper()[0]
    if opc == 'N':
        break
print(10*'-=')
print(f'''lista completa = {lista}
lista de pares = {par}
lista de impares = {impar}''')
