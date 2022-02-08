#Crie um programa que leia vários números inteiros pelo teclado. O programa so vai parar quando o usúario digitar o valor 999
#que é a condição de parada. No final mostre quantos números foram dgitados e qual foi a soma entre eles(desconsiderando o flag).
cont = soma = 0
while True:
    num = int(input('Digite um número: [Digite 999 para parar]'))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} valores foi {soma}')