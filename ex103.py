def ficha(j='-desconhecido-', g=0):
    print(f'O jogador {j} fez {g} gol(s)')


jogador = input('Nome do jogador: ').strip()
gols = str(input('Numero de gols: ')).strip()
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if len(jogador) == 0:
    ficha(g=gols)
else:
    ficha(j=jogador, g=gols)
