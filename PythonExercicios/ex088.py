#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados
#e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
print('-' * 40)
print(f'{"JOGAR NA MEGA SENA":^40}')
print('-' * 40)
lista = list()
cont = tot = 1
quant = int(input('Quantos números você quer eu sorteie ? '))
print(f'{"-=" * 5} SORTEANDO {quant} JOGOS {"-=" * 5}')
while not cont > quant:
    while not tot > 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            tot += 1
    print(f'Jogo {cont}: {sorted(lista)}')
    sleep(1)
    lista.clear()
    cont += 1
    tot = 1
print('-=' * 19)
