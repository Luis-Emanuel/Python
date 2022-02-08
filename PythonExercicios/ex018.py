#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
an = int(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
coss = cos(radians(an))
tang = tan(radians(an))
print(f"O ângulo de {an} tem o SENO de {seno:.2f} \nO COSSENO de {coss:.2f} \nA TANGENTE de {tang:.2f} ")