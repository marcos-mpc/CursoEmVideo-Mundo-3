print(15*'_-')
print('ANALIZANDO TABELA BRASILEIRÃO')
print(15*'_-')
tabela = ('Bragantino', 'Athletico-PA', 'Palmeiras', 'Fortaleza', 'Bahia', 'Santos', 'Atlético-GO', 'Atlético-MG',
          'Fluminense', 'Flamengo', 'Corinthians', 'Ceará SC', 'Internacional', 'Juventude', 'Sport Recife', 'Cuiabá',
          'São Paulo', 'Chapecoense', 'América-MG', 'Grêmio')
print(f'Os 5 Primeiros Colocados São: {tabela[0:5]}')
print(30*'-')
print(f'Os Ultimos 4 Colocados São: {tabela[-4:]}')
print(30*'-')
print(f'Nome Em Ordem Alfabética: {sorted(tabela)}')
print(30*'-')
print(f'A Chapecoense Está Na Posição {tabela.index("Chapecoense")+1}ª')
