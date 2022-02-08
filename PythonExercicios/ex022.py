#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem consderar espaços)
#Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo:')).strip()
nomes = nome.split()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format( nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome é {} ele tem {} letras'.format(nomes[0], len(nomes[0])))
