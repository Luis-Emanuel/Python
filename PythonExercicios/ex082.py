#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter
#apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
for p, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('-=' * 20)
print(f'A lista completa é {num} ')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
print('-=' * 20)
