#Crie um programa que tenha uma função fatorial() que recebe dois parâmetros: o primeiro que indique o número a calcular
#e o outro chamado show, que será um valor lógico(opcional) indicando se será mostradddo ou não na tela o processo de
#cálculo do fatorial.
def fatorial(num=0, show=False):
    """
    ->Cálcula o fatorial de um número.
    :param num: O número que será fatorado
    :param cal: (opcional) Mostra conta de fatoração
    :return: O valor do fatoração dee um número
    """
    cont = 1
    for c in range(num, 0, -1):
        cont *= c
        if show == True:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return cont


print(fatorial(5, True))
help(fatorial)
