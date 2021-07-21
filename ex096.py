print(f'{20*"="}\n{"ÁREA DE TERRENO"}\n{20*"="}')


def area(a, b):
    print(30*'=')
    print(f'com a largura de {a:.2f}m e comprimento de {b:.2f}m temos uma área de {a * b:.2f}m²')
    print(30*'=')


area(a=float(input('Largura (m): ')), b=float(input('Comprimento (m): ')))
