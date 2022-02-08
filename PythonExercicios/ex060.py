#Faça um programa que leia um número qualquer e mostre seu fatorial.
c = int(input('Digite um número para fatorar: '))
f = 1
while c > 0:
    f *= c
    print('{}'.format(c), end='')
    c -= 1
    print(' x ' if c > 1 else ' = ', end='')
print(f)