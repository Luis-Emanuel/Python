#Crie um programa que leia vários números inteiros pelo teclado. O programa so vai parar quando o usuário digitar 999, que é
#a condicão de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o 999)
num = 0
c = 0
soma = 0
num = int(input('Dígite um número [999 para parar]: '))
while num != 999:
    soma += num
    c += 1
    num = int(input('Dígite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(c, soma))