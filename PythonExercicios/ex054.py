#Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas
# ainda não atingiram a maior idade e quantas já são maiores
from datetime import date
idade_a = 0
idade_m = 0
for c in range(1, 8):
    nasc = int(input('Digite a data de nascimento da {} pessoa: '.format(c)))
    idade = date.today().year - nasc
    if idade >= 18:
        idade_a += 1
    else:
        idade_m += 1
print('Um total de {} pessoas são maiores de idade'.format(idade_a))
print('Um total de {} pessoas são menores de idade'.format(idade_m))
