#Crie um program que leia o nome de uma pessoa e diga se ela tem 'SILVA" no mome
nome = str(input('Qual o seu nome completo? ')).strip().upper()
print('Seu nome tem Silva? {}'.format('SILVA' in nome))