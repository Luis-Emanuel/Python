#Crie um programa que leia o nome e o  preço de vários produtos. O program ddeverá perguntar se o usuário vai continuar.
#No final, mostre: A) Qual é o total gasto na compra B)Quantos produtos custão mais que 1000 C)Qual é o nome do produto mais barato.
cont = soma = produto_mais = produtovalor = 0
produto_menos = ''
print(20*'-')
print('{:^20}'.format('LOJAS MARANHÃO'))
print(20*'-')
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço R$: '))
    soma += preco
    cont += 1
    if preco > 1000:
        produto_mais += 1
    if cont == 1 or produtovalor > preco:
        produto_menos = nome
        produtovalor = preco
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(20*'=')
print(f'O total do valor foi R${soma:.2f}')
print(f'Temos {produto_mais} produtos que custão mais de R$1000.00')
print(f'O produto mais barato foi {produto_menos} que custa R${produtovalor:.2f}')
