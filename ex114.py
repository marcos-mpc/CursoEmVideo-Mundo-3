import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Erro! Não foi possivel o acesso.')
else:
    print('site acessivel!')
