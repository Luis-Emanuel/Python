# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mosttre a área do terreno.
def linha():
    print('-' * 20)


def area(lar, com):
    a = lar * com
    print(f'A área de um terreno {lar} X {com} é de {a}m²')


linha()
print('CONTROLE DE TERRENOS')
linha()
lar = float(input('LARGURA (m): '))
com = float(input('COMPRIMENTO (m): '))
area(lar, com)
print('FIM')
linha()
