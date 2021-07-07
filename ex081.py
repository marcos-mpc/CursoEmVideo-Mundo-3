print(30*'-')
print(f'{"examinando lista":^30}')
print(30*'-')
lista = list()
while True:
    lista.append(int(input('digite um numero: ')))
    opc = input('continuar ? [S/N] ')
    if opc[0] in 'Nn':
        break
print(30*'=')
print(f'foram digitados {len(lista)} numeros')
print(f'lista de forma decrescente é {sorted(lista,reverse=True)}')
if 5 in lista:
    print('o valor 5 foi digitado')
else:
    print('o valor 5 nao foi digitado')
