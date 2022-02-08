#Crie um programa que leia nome, sexo e idade de vários pessoas, guardando os dados de cada peessoas em um dicinário
#em um lista. No final, mostre: A) Quantas pessoas cadastro.  B) A média de idade. C) Uma lista com mulheres.
#D)Uma lista com idade acima da média.
cadastros = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    cadastros.append(pessoa.copy())
    pessoa.clear()
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
media = soma / len(cadastros)
print('-='*20)
print(f'A) Ao todo temos {len(cadastros)} pessoas cadastradas.')
print(f'B) A média de idade é de {media}')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in cadastros:
    if p['sexo'] in 'F':
        print(f' {p["nome"]} |', end='')
print('\nD) Lista das pessoas que estão acima da média: ', end='')
for p in cadastros:
    if p['idade'] > media:
        print(f' {p["nome"]} |', end='')
print('-=' * 20)
