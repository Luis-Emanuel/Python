#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
#mostre uma listagem de preços, organizando os dados em forma tabular.
lista = ('Suport', 65.5,
         'Caneca', 45.70,
         'Monitor', 3.500,
         'Tecaldo', 187.90,
         'Mouse', 56.50,
         'Camera', 252.90)
print('--'*20)
print('{:^40}'.format('LISTA DE PREÇO'))
print('--'*20)
for pos in range(len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<40}', end='')
    else:
        print(f'R${lista[pos]:>}')
print('--'*20)
