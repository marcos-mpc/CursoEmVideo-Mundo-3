print(10*'-_')
print(f'{"PROCURANDO VOGAIS":^20}')
print(10*'-_')

lista = ('marcos', 'fernando', 'matheus', 'lucas', 'beathris', 'nathalia', 'nadia', 'cybeli',
         'natah', 'fabricio', 'carlos', 'julia', 'amanda', 'thais', 'silvia')

for v in lista:
    print(f'\nNa palavra {v.upper()} temos as vogais ', end='')
    for palavra in v:
        if palavra.lower() in 'aeiou':
            print(palavra, end=' ')
