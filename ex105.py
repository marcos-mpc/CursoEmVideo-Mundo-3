def notas(*n, sit=False):
    """
    => Função para analisar as notas e situações de alunos.
    :param n: uma ou mais notas dos alunos (varios valores aceitos)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dic = {'Total': len(n), 'Maior': max(n), 'Menor': min(n), 'Média': (sum(n)/len(n))}
    if sit:
        if dic['Média'] < 6:
            dic['Situação'] = 'Ruim'
        elif 6 <= dic['Média'] < 7:
            dic['Situação'] = 'Razoável'
        elif dic['Média'] >= 7:
            dic['Situação'] = 'Boa'

    return dic


print(notas(7, 5, sit=True))
