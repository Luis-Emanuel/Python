#Desenvolva um programa que leia o primeiro termo de uma PA. No final mostre os 10 primeiros termos dessa progressão.
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = p + (10 - 1) * r
for c in range(p, d + r, r):
    print('{}'. format(c), end= ' -> ')
print('ACABOU')
