#Faça um programa que leia 5 valores númericos e guarde-os em lista. No final, mostre qual foi o maior e o menor valor
#digitado e as suas respectivas posições na lista.
num = []
maior = 0
menor = 0
for c in range(0, 5):
    num.append(int(input(f'Digite o {c+1}° valor:')))
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print('-=' * 30)
print(f'Os números digitados foram {num}')
print(f'O MENOR valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}... ', end='')
print(f'\nO MAIOR valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}... ', end='')
print('\nFIM')
print('-=' * 30)