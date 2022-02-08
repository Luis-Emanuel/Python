#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando estrutura while.
num = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 0
while c < 10:
    num += r
    print('{} -> '.format(num), end='' )
    c += 1
print('FIM')
