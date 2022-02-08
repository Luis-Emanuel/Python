#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#-Abaixo de 18.5: ABAIXO_DO_PESO             - 25 até 30: SOBREPESO
#-Entre 18.5 e 25: PESO_IDEAL                - 30 até 40: OBESIDADE
#                                            - Acima de 40: OBESIDADE_MÓRBIDA
peso = float(input('Qual o seu peso: '))
alt = float(input('Qual a sua altura: '))
imc = peso /( alt ** 2)
print(f'O IMC é de {imc:.1f}')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 < imc < 30:
    print('SOBREPESO')
elif 30 < imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')