#Crie um programa que vai ler cários númros e colocar em uma lista. Depois disso, mostre:A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 fou digitado e está ou não na lista.
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Você deseja adicionar outro valor ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 20)
print(f'Os valores digitados foram: {lista}')
print(f'A quantidade de números na lista e {len(lista)}')
lista.sort(reverse=True)
print(f'Os valores em forma decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 nao foi encontrado.')
print('FIM')
