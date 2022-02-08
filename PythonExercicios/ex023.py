#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#EX Digite um número: 1834 undade: 4 dezenas: 3 centena: 8 milhar: 1
num =int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centanas: {}'.format(c))
print('Milhares: {}'.format(m))
