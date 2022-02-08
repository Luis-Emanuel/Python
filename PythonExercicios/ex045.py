#Crie um programa que faça o computador jogar jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0,2)
print('''Suas  opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Qual é a sua jogada ? "))
print('JO')
sleep(1)
print('KE')
sleep(1)
print('PO!!!')
sleep(1)
print(20*'-=')
print('''Computador jogou {}
Jogador jogou {}'''.format(itens[comp], itens[jogador]))
print(20*'-=')
if comp == 0:  # PEDRA
    if jogador  == 0:
        print('EMAPATE')
    elif jogador == 1:
        print('VITORIA DO JOGADOR')
    elif jogador == 2:
        print('VITORIA DO COMPUTADOR')
elif comp == 1: #PAPEL
    if jogador == 0:
       print('VITORIA DO COMPUTADOR')
    elif jogador == 1:
        print('EMAPATE')
    elif jogador == 2:
        print('VITORIA DO JOGADOR')

elif comp == 2: #TESOURA
    if jogador == 0:
        print('VITORIA DO JOGADOR')
    elif jogador == 1:
        print('VITORIA DO COMPUTADOR')
    elif jogador == 2:
        print('EMAPATE')
