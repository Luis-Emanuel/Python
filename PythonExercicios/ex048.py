#Faça um programa que calcule a soma entre todos os impares que são múltiplos
# de três e que se encontram no intervalo de 1 até 500.
s = 0
cont = 0
for c in range(1,500):
    if c % 2 == 1 and c % 3 == 0:
        print('O numero {} '.format(c))
        s += c
        cont += 1
print('A soma de todos os {} valores {}'.format(cont, s) )
