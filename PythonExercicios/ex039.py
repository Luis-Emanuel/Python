#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, seela ainda vai se alistar
#ao serviço militar, se é a hora  de se alistar ou sejá passou do tempo do alistamento. Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.
from datetime import date
sexo = str(input('Qual o seu sexo: [M/F]').strip().upper())

if sexo == 'M':
    nasc = int(input('Ano de nascimento:'))
    atual = date.today().year
    idade = atual - nasc
    if  idade > 18:
        saldo = idade - 18
        print(f'Você ja deveria ter se apresentado em {(atual - saldo)}.')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Você ainda não esta com idade, volte em {(saldo + atual)}.')
    else:
        print('Você tem que se alistar imediatamente!')
else:
    print('O seu alistamento não e obrigatorio ')
