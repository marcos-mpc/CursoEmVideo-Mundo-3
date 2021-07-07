print(20*'=')
print('EXAMINANDO EXPREÇÃO')
print(20*'=')
cont1 = cont2 = 0
ex = input('digite a expreção: ')
for c in ex:
    for f in c:
        if f == '(':
            cont1 += 1
        elif f == ')':
            cont2 += 1
if cont1 == cont2:
    print('sua expreção está correta!')
else:
    print('sua expreção está errada!')
