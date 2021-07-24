def voto(ano):
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        return f'com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'com {idade} anos: VOTO OBRIGATÓRIO.'


nasc = int(input('Digite o ano de nascimento: '))
print(voto(nasc))
