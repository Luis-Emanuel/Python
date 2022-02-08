#Desenvolva um programa que leia  o nome, idade e sexo de 4 pessoas. No final mostre:
# - A média de idade do grupo.                  - Quantas mulheres tem menos de 20 anos.
# - Qual é nome do homem mais velho.
totidade = 0
i_velho = 0
nome_velho = ''
totm = 0
for c in range(1, 5):
    print(5*'-', '{} pessoa'.format(c), 5*'-')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    totidade += idade
    if c == 1 and  sexo == 'M':
        i_velho = idade
        nome_velho = nome
    elif idade > i_velho and sexo == 'M':
        i_velho = idade
        nome_velho = nome
    elif sexo == 'F' and idade < 20:
        totm += 1
print('A  média de idade do grupo é de {} anos'.format(totidade/c))
print('o homem mais velho tem {} anos e se chama {}.'.format(i_velho, nome_velho))
print('Ao total são {} mulheres com menos de 20 anos'. format(totm))
