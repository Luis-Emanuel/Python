#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números
#gerados também indique o maior e o menor valor que estão na tupla.
from random import randint
num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os valores sorteados foram: {num}')
print(f'O maior valor sorteado  foi {max(num)}')
print(f'O menor sorteado foi {min(num)}')

