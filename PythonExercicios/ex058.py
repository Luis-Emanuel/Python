#Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
#ter que tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer.
from random import randint
j = int(input('Estou pensando em um número entre 1 e 10, tente adivinhar :'))
pc = randint(0, 10)
tot = 1
while not j == pc:
    tot += 1
    if j > pc:
      j = int(input('Tente um valor menor:'))
    else:
      j = int(input('Tente um valor maior:'))
print('Você acertou em {} tentativas.'.format(tot))
