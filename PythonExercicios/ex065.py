#Crie um programa que leia vários números inteiros pela tecla. No final da execução, mostre a média entre todos os valores
#e qual foi o maior e o menor valores lidos. O O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
c = 0
soma = 0
resp = 'S'
while resp == 'S':
    num = int(input('Digite um número: '))
    soma += num
    c += 1
    if c == 1:
        maior = num
        menor = num
    elif num < menor:
        menor = num
    elif num > maior:
        maior = num
    resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
print('Você digitou {} números e a média foi de {}'.format(c, (soma/c)))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))