time = list()
jogador = dict()
partida = list()

while True:
    jogador.clear()
    jogador['nome'] = (input('nome do jogador: '))
    tot = int(input(f'quantas partidas {jogador["nome"]} jogou? '))
    partida.clear()
    for c in range(0, tot):
        partida.append(int(input(f'   quantos gols na partida {c+1}? ')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N. ')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:>15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogardo ? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Nao existe jogador com codigo {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< Volte Sempre >>')
