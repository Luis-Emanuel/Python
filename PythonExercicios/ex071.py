#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual o será o valor
# a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#Considere que o caixa  possui cédulas de R$50, R$20, R$10 e R$1
cont_50 = cont_20 = cont_10 = cont_1 = 0
print(30*'=')
print('{:^30}'.format('BANCO DO BRASIL'))
print(30*'=')
num = int(input('Qual valor deseja ser sacado? '))
while num >= 50:
    num -= 50
    cont_50 += 1
while num >= 20:
    num -= 20
    cont_20 += 20
while num >= 10:
    num -= 10
    cont_10 += 1
while num >= 1:
    num -= 1
    cont_1 += 1
print(f'Total de {cont_50} cédulas de R$50')
print(f'Total de {cont_20} cédulas de R$20')
print(f'Total de {cont_10} cédulas de R$10')
print(f'Total de {cont_1} cédulas de R$1')
print(30*'=')
print('Volte sempre ao BANCO DO BRASIL! Tenha um bom dia.')