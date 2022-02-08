#Faça um program que leia o nome completo de uma pessoa, mostrando em seguinda o primeiro e último nome separados.
#EX: Ana Maria de Sousa/ primeiro = Ana/ segundo = Sousa
nome = str(input('Digite seu nome completo: ')).strip().upper()
nomes = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nomes[0]))
print('Seu último nome é {}'.format(nomes[len(nomes) - 1]))
