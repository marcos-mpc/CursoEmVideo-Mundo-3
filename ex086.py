print(10*'-=')
print(f'{"MATRIZ 3*3":^20}')
print(10*'-=')
lista = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        lista[c].append(int(input(f'posição [{l}:{c}] = ')))
print(f'[{lista[0][0]}][{lista[0][1]}][{lista[0][2]}]')
print(f'[{lista[1][0]}][{lista[1][1]}][{lista[1][2]}]')
print(f'[{lista[2][0]}][{lista[2][1]}][{lista[2][2]}]')
