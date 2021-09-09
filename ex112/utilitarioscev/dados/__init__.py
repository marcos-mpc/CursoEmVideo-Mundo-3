def inputar(n):
    num = 0
    while True:
        txt = str(input(n)).replace(',', '.').strip()
        if txt.isalpha() or txt == '':
            print(f'\033[31mErro! \"{txt}\" nao é um valor monetario.\033[m')
        else:
            num = float(txt)
            break
    return num
