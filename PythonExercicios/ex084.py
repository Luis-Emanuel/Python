#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas. B)Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
dados = list()
grupo = list()
pesada = list()
leve = list()
cont = maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    grupo.append(dados[:])
    if cont == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] >= maior:
            maior = dados[1]
        if dados[1] <= menor:
            menor = dados[1]
    dados.clear()
    cont += 1
    resp = str(input('Você quer adicionar mais ? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
for n, p in grupo:
    if menor == p:
        leve.append(n)
    if maior == p:
        pesada.append(n)
print('-='*30)
print(f'{cont} pessoas foram cadastradas.')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de {pesada} ')
print(f'O menor peso foi de {menor:.1f}Kg. Peso de {leve} ')
