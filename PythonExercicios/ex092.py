#Crie um programa que leia nome, ano de nascimento e carteiro de trabalho e cadastre-os(com idade) em dicionário se por
#acaso a CTPS for diferente de ZERO, o dicionário  receberá também o ano de contração e o salário. Calcule e acresente,
#além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
cadastro = dict()
cadastro['nome'] = str(input('NOME: '))
ano = int(input('Ano de nascimento: '))
cadastro['idade'] =datetime.now().year - ano
cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contrato'] = int(input('Ano de contratação: '))
    cadastro['Salario'] = int(input('Salário: R$'))
    cadastro['Aposetadoria'] =cadastro['idade'] + ((cadastro['contrato'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in cadastro.items():
    print(f'- {k} tem o valor {v}')
print('=' * 30)
