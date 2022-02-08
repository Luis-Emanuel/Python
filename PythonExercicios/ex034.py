#Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
#Para salário acima de 1.250,00, calcule um almento de 10%. Para os inferiores ou iguais, o aumento é de 15%
sal = float(input('Qual o salario do funcionário?R$ '))
if sal <= 1250:
    novo_sal = sal + (sal * 15 /100)
else:
    novo_sal = sal + (sal * 10 /100)
print(f'Quem ganhava R${sal:.2f} passa a ganhar R${novo_sal:.2f}')