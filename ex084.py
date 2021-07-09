lista = []
listtemp = []
pespesada = []
pesleve = []
cont = maipes = menspes = 0

while True:
    nome = input('digite seu nome: ')
    peso = float(input('digite seu peso: '))
    listtemp.append(nome)
    listtemp.append(peso)
    lista.append(listtemp[:])
    listtemp.clear()
    if cont == 0:
        maipes = peso
        pespesada.append(nome[:])
        menspes = peso
        pesleve.append(nome[:])
    else:
        if peso > maipes:
            pespesada.clear()
            maipes = peso
            pespesada.append(nome[:])
        else:
            if peso == maipes:
                maipes = peso
                pespesada.insert(-1, nome)
        if peso < menspes:
            pesleve.clear()
            menspes = peso
            pesleve.append(nome[:])
        else:
            if peso == menspes:
                menspes = peso
                pesleve.insert(-1, nome)
    cont += 1
    opc = input('deseja continhar ? [S/N] ')
    if opc[0] in 'Nn':
        break

print(f'foram cadastradas {cont} pessoas.')
print(f'o maior peso foi de {maipes}kg que pertence a {pespesada}')
print(f'o menor peso foi de {menspes}kg que pertence a {pesleve}')
