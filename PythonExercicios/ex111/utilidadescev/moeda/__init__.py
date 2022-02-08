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
    formatado = f'{moeda}{preco:.2f}'.replace('.', ',')
    return formatado


def resumo(p=0, acrecimo=10, redução=5):
    print('--' * 15)
    print(f'{"RESUMO DE VALOR":^30}')
    print('--' * 15)
    print(f'Preço analisado:\t{moeda(p):<}')
    print(f'Dobro preço:\t\t{dobro(p, True):<}')
    print(f'Metade do preço:\t{metade(p, True):<}')
    print(f'{acrecimo}% de aumento:\t\t{aumentar(p, acrecimo, True):<}')
    print(f'{redução}% de redução:\t\t{diminuir(p, redução, True):<}')
    print('--' * 15)
