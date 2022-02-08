#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80kmH, mostre uma messagem
#dizendo que ele foi mutado. A multa vai custar R$7,00 por cada Km acima do limite.
vel = float(input('Qual é a velocidade atual do carro? '))
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    mul = (vel - 80) * 7
    print(f'Você deve pagar uma multa de R${mul:.2f}')
print('Tenha um bom dia! Dirija com segurança!')
