#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
#boletim contendo a média de cada um e permita que o usuário porra mostrar as notas de cada aluno individualmente.
boletim = list()
opc = 0
while True:
    nome = str(input('NOME: '))
    nota1 = float(input('NOTA_1: '))
    nota2 = float(input('NOTA_2: '))
    media = (nota1 + nota2)/ 2
    boletim.append([nome, [nota1, nota2], media])
    resp = str(input('Você quer adicionar aluno ? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
print('-' * 40)
while opc != 999:
    opc = int(input('Digite o "No" de qual aluno você deseja ver as notas ? [Digitar 999 finaliza o programa]'))
    if opc <= len(boletim) - 1:
       print(f'Aluno {boletim[opc][0]} --> {boletim[opc][1]}')
print('-=' * 40)
