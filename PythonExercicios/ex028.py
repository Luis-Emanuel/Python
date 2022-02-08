#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador. O pragrama deverá escreveu na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print('-='*30, '\nVou pensar e um número entre 0 e 5. Tente advinhar...\n', '-='*30)
m = randint(0,5)                                             #Faz computador "PENSAR"
j = int(input('Em que número eu pensei?'))                   #Jogador tentando adivinhar
print('PROCESSANDO...')
sleep(3)
if j == m:
    print('VOCÊ GANHOU!')
else:
    print(f'GANHEI!Eu pensei no nùmero {m} e não no {j}')
