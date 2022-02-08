#Faça um programa que leia o sexo de uma pessoas, mas só aceite valores 'M' e 'F'.
#Caso esteja errado, peça a digitação novamente até terum valor correto.
sexo = str(input('Informe o sexo: [M/F]')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados invalidos, Por favor infome seu sexo: ')).strip().upper()[0]
if sexo == 'M':
    print('o sexo é Masculino')
else:
    print('O sexo é Feminino')