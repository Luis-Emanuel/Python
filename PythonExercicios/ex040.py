#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERACÃO
# - Média 7.0 ou superior: APROVADO
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
med = (nota1 + nota2) / 2
print(f'Sua média foi {med:.1f}')
if med <= 5.0:
    print('Reprovado')
elif 6.9 >= med >= 5 :
    print('Recuperação')
else:
    print('Aprovado')