#ESSA FOI A MINHA TENTATIVA DE SOLUÇÃO USANDO 'for in renge'
from time import sleep
def cont(i = 0, f = 0, p = 0):
    print('-=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p == 0:
        p = 1
    if p < 0:
        for c in range(i, f+1, p):
            print(f'{c} ', end='')
            sleep(0.2)
    elif i <= f:
        for c in range(i, f+1, p):
            print(f'{c} ', end='')
            sleep(0.2)
    elif i > f:
        p *= -1
        for c in range(i, f+p, p):
            print(f'{c} ',end='')
            sleep(0.2)
    print('FIM')


cont(1, 10, 1)
cont(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('INÍCIO: '))
f = int(input('FIM:    '))
p = int(input('PASSO:  '))
cont(i, f, p)
