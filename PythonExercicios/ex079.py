#Crie um programa onde o  usuário possa digitar vários valores números e cadastre-os  em uma  lista. Caso o número já
#já exista lá dentro, ele não será  adicionado. No final, serão exibidos todos os valores únicos digitos, em ordem crescente.
lista = []
c = 0
while True:
    num = int(input('Digite um valor:'))
    if num in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(num)
    resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        print('-=' * 20)
        break
    c += 1
print(f'Você digitou os valores: {sorted(lista)}')