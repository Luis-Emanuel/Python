#Crie um programa que  leia  quanto dinheiro uma pessoa na carteira  e mostre quantos Dólares ela pode compra ?
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dol = real / 5.56
print('Com {:.2f} R$ você pode compra US${:.2f} '.format(real, dol))
