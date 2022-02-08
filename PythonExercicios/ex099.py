#Faça um programa que tenha uma fução chamada maior(), que receba vários parâmetros com valores interios. Seu programa
#tem que analisar todos os valores e dizer qual deles é o maior.
def numeros(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


numeros(2, 9, 4, 5, 7, 1)
numeros(4, 7, 0)
numeros(1, 2)
numeros(6)
numeros()

