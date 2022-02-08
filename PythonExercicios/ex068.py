#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogar perder, mostre
#o toral de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
cont = 0
resp = ''
while True:
    num = int(input('Digite um número: '))
    num_pc = randint(1,10)
    soma = num + num_pc
    jg = str(input('Par ou Ímpar: [P/I]')).strip().upper()[0]
    if soma % 2 == 0:
        resp = 'P'
    else:
        resp = 'I'
    print(f'Você jogou {num} e o computador {num_pc}. Total de {soma} deu {resp}')
    if jg == resp:
        print('Você GANHOU')
        cont += 1
    else:
        print('Você PERDEU')
        break
print(f'GAME OVER! Você venceu {cont} vezes.')