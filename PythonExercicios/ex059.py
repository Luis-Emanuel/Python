#Crie um programa que leia dois valores e mostre um menu. Seu programa deverá realizar a operação solicitada em cada caso.
#[1] soma [2] multiplicar [3] maior [4] novos números [5] sair do programa.
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
esc = 0
while esc != 5:
    print('''-=-=-=--=-=-=-=-=-=-=--=-=-=
        [1] SOMA
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIR DO PROGRAMA''')
    esc = int(input('>>>>Qual é sua opção: '))
    if esc == 1:
        print('A soma entre {} + {} = {}'.format(num1, num2, num1 + num2))
    elif esc == 2:
        print('A multiplicação entre {} x {} = {}'.format(num1, num2, num1 * num2))
    elif esc == 3:
        if num1 > num2:
            print('Entre {} e {} o maior é {}'.format(num1, num2, num1))
        else:
            print('Entre {} e {} o maior é {}'.format(num1, num2, num2))
    elif esc == 4:
        num1 = int(input('Digite o novo valor: '))
        num2 = int(input('Digite o outro valor: '))
    elif esc == 5:
        print('Fim')
    else:
        print('___OPÇÃO INVALIDA___')