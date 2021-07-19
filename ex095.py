print(f'{20*"="}\n{"ANALIZANDO JOGADORES"}\n{20*"="}')
jogadores = list()
dados = dict()
gols = list()
while True:
    dados['nome'] = input('Nome: ')
    partidas = int(input('Numero de partidas:  '))
    for c in range(0, partidas):
        gols.append(int(input(f'  - Numero de gols na partida {c}: ')))
    dados['gols'] = gols.copy()
    dados['total de gols'] = sum(gols)
    jogadores.append(dados.copy())
    gols.clear()
    opc = input('Deseja continuar? [S/N]')
    while opc not in 'SsNn':
        opc = input('opção errada! responda S ou N')
    if opc in 'Nn':
        break
print(jogadores)
print(32*'=')
print(f'{"TABELA":^32}')
print(32*'=')
print(f'{"cod":<5}{"nome":<10}{"gols":<10}{"total"}')
print(32*'-')
for c in range(0, len(jogadores)):
    print(f'{c:<5}{jogadores[c]["nome"]:<10}{jogadores[c]["gols"]}{jogadores[c]["total de gols"]}')
while True:
    print(32 * '-')
    lev = int(input('Deseja ver dados de qual jogador? 999 encerra: '))
    if lev == 999:
        break
    for c in range(0, len(jogadores[lev]['gols'])):
        print(f'na partida {c+1} foi feito {jogadores[lev]["gols"][c]} gols')
print(32*'-')
print('PROGRAMA FINALIZADO!')
