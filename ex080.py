print(20*'=')
print(f'{"lista em ordem":^20}')
print(20*'=')

lista = []
for n in range(0, 5):
    num = int(input('digite um numero: '))
    if n == 0 or num > lista[-1]:
        lista.append(num)
        print('adicionado ao ultimo da fila')
    else:
        ver = 0
        while ver < len(lista):
            if num <= lista[ver]:
                lista.insert(ver, num)
                print(f'adicionado na posição {ver}')
                break
            ver += 1
print(f'a lista final é {lista}')
