def aumentar(au, taxa):
    val = au + ((au * taxa) / 100)
    return val


def diminuir(di, taxa):
    val = di - ((di * taxa) / 100)
    return val


def dobro(do):
    do *= 2
    return do


def metade(me):
    me /= 2
    return me
