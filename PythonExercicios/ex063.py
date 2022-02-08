#Escreva que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos da Sequência de Fibonacci
#Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 -> 13 ....
print(20*'-')
print('Seguencia de Fibonacci')
print(20*'-')
n = int(input('Quantos termos você  que mostra ? '))
c = 3
t1 = 0
t2 = 1
print('{} -> {} -> '.format(t1,t2), end='')
while c <= n:
    t3 = t2 + t1
    t1 = t2
    t2 = t3
    print(' {} -> '.format(t3), end='')
    c += 1