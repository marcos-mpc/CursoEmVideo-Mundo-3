print(37*'=')
print(f'{"TABELA DE PREÇOS":^37}')
print(37*'=')
produtos = ('arroz', 4.50, 'feijão', 5, 'macarrão', 2.30, 'farinha', 3, 'leite', 4.50, 'nescal', 3.75,
            'batata', 2, 'cebola', 2, 'macaxeira', 2.50, 'tomate', 5, 'mortadela', 8.15,
            'salsicha', 9.80, 'danone', 8.80, 'calabresa', 9.20, 'agua sanitária', 1.30, 'farinha de trigo', 3.40,
            'sal', 0.80, 'açucar', 3.30, 'coloral', 2, 'beterraba', 2, 'goma', 3, 'alface', 3.80)

for p in range(0, len(produtos)):
    if p % 2 == 0:
        print(f'{produtos[p]:.<30}', end='')
    else:
        print(f'R$ {produtos[p]:.2f}')
