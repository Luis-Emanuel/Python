#Faça um programa que tenha uma função chamada finha(), que receba dois parâmetros opcionais: o nome de um jogagdor e
#quantos gols ele marcou. O programa deverá ser capaz de mostrar a finha do jogador, mesmo que algum dado não tenha
#sido informado corretamente.
ficha = list
def tabela(jogador='<desconhecido>', gols=0):
        return (f'O jogagdor {jogador} fez {gols} gol(s) no campeonato')


nome = str(input('Nome do Jogador: '))
gol = str(input('Número de gols: '))
if gol.isnumeric():
        gol = int(gol)
else:
        gol = 0
if nome.strip() == '':
        print(tabela(gols=gol))
else:
        print(tabela(nome, gol))

