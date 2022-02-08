def aumentar(au=0, taxa=0, show=False):
    au = au + ((au * taxa) / 100)
    if show == True:
        au = moeda(au)
    return au


def diminuir(di=0, taxa=0, show=False):
    di = di - ((di * taxa) / 100)
    if show == True:
        di = moeda(di)
    return di


def dobro(do=0, show=False):
    do *= 2
    if show == True:
        do = moeda(do)
    return do


def metade(me=0, show=False):
    me /= 2
    if show == True:
        me = moeda(me)
    return me


def moeda(preco=0, moeda= 'R$'):
    formatado = f'{preco:.2f}{moeda}'.replace('.', ',')
    return formatado
