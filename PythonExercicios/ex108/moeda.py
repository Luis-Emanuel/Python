def aumentar(au=0, taxa=0):
    val = au + ((au * taxa) / 100)
    return val


def diminuir(di=0, taxa=0):
    val = di - ((di * taxa) / 100)
    return val


def dobro(do=0):
    do *= 2
    return do


def metade(me=0):
    me /= 2
    return me


def moeda(preco=0, moeda= b'R$'):
    formatado = f'{preco:.2f}{moeda}'.replace('.', ',')
    return formatado