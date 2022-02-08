#Crie um programa que leia a idade e o sexo de várias pessoas. A cada cadastro. o programa deverá perguntar ao usuário
#quer ou não continuar. No final, mostre: A) Quantas pessoas tem mais de 18 anos. B) Quantos homens foram cadastrados.
#C) Quantas mulhres tem menos dde 20 anos
homem = mulher = mais_idade = 0
while True:
    print(40*'-')
    print('{:^40}'.format('CADASTRE UMA PESSOA'))
    print(40*'-')
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo =  str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade > 18:
        mais_idade += 1
    if sexo == 'M':
        homem += 1
    if idade < 20 and sexo == 'F':
        mulher += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pesssoas com mais  de 18 anos: {mais_idade}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher} mulhres com menos de 20 anos')

