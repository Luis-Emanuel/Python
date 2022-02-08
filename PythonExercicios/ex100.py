#Faça um programa que tenha um lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
#vai sortear 5 números e vai colocá-las dentro da lista e a segunda função vai mostrar a soma entre todos os valores
#PARES sorteados pela função anterios.
from random import randint
from time import sleep
numeros = list()


def sortear(valor):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        num = randint(1, 10)
        print(f'{num}, ', end='')
        sleep(0.3)
        valor.append(num)
    print('PRONTO!')


def somapar(soma_pares):
    s = 0
    print(f'Somando os valores pares de {soma_pares}, temos ', end='')
    for c in soma_pares:
        if c % 2 == 0:
            s += c
    print(s)

sortear(numeros)
somapar(numeros)