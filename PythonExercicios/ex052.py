#Faca um programa que leia um número inteiro e digite se ele é ou não um número primo.
num = int(input('Digiite o número: '))
tot = 0
for c in range(1, num +  1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m',  end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi dividido {} vezes.'.format(num, tot))
if tot == 2:
    print('ELE É UM NÚMERO PRIMO')
else:
    print('NÃO É UM NÚMERO PRIMO')
