#Faça um programa que leia o salário de um funciona´rio e mostre seu novo salário, com 15% de aumento.
sal = float(input('Qual o salário do funcionário? R$'))
novo_sal = sal + (sal * 15 / 100)
print('Um funcionário que ganhava R${}, com 15% de aumento passou a receber R${}'.format(sal, novo_sal))
