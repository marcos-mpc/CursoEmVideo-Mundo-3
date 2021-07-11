from random import randint
from time import sleep
print(15*'-=')
print(f'{"PALPITES MEGA SENA":^30}')
print(15*'-=')
palpite = []
temp = []
x = int(input('quantos palpites vc quer ? '))
for c in range(0, x):
    for n in range(0, 6):
        num = randint(1, 60)
        if n != 0:
            for p in temp:
                if num == p:
                    num = randint(1, 60)
        temp.append(num)
    palpite.append(temp[:])
    temp.clear()
print(30*'=')
for pal in palpite:
    print(pal)
    sleep(1)
print(30*'=')
