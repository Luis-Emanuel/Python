#Faça  um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
valor = float(input('Qual o preço do produto: R$'))
preco_novo = valor - (valor * 5)/100
print('O produto que custa R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(valor, preco_novo))
