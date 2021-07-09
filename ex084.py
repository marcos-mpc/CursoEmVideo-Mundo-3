lista = []
listtemp = []
pesado = []
leve = []
cont = pes = lev = 0
while True:
    listtemp.append(input('digite seu nome: '))
    listtemp.append(int(input('digite seu peso: ')))
    lista.append(listtemp[:])
    listtemp.clear()
    cont += 1
    opc = input('deseja continhar ? [S/N] ')
    if opc[0] in 'Nn':
        break
for c in range(0, cont):
    if lista[c][1] >= 100:
        pes += 1
        pesado.append(lista[c][0])
    elif lista[c][1] <= 70:
        lev += 1
        leve.append(lista[c][0])
print(15*'-=')
print(f'foram cadastradas {cont} pessoas.')
print(f'{pes} pessoas são pesadas que são {pesado}')
print(f'{lev} pessoas são leves que são {leve}')
