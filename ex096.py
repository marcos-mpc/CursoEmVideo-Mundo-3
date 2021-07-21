def aria(a, b):
    print(30*'=')
    print(f'com a largura de {a:.2f}m e comprimento de {b:.2f}m temos uma ária de {a * b:.2f}m²')
    print(30*'=')


aria(a=float(input('Largura (m): ')), b=float(input('Comprimento (m): ')))
