#Desenvolva um programa que pergunte a distância de uma viajem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,40 para viagens mais longas.
dis = float(input('Qual a distancia da viajem:'))
print(f'Você esta preste a começar uma viajem de {dis}Km')
if dis < 200:
    preco = 0.50 * dis
else:
    preco = 0.40 * dis
print(f'E o preço da sua passagem será de R${preco:.2f}')