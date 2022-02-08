#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: Dite um número: 6.127
#O número 6.127 tema parte inteira 6.
from math import trunc
num = float(input('Digite o número: '))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
