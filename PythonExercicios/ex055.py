#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual o maior e o mneor peso lidos.
maior = 0
menor = 0
for c in range(1, 6):
  peso = float(input('Peso da {} pessoa: '.format(c)))
  if c == 1:
    maior = peso
    menor = peso
  elif peso > maior:
    maior = peso
  elif peso < menor:
        menor = peso
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))