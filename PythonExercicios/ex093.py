#Crie um programa que gentencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantos
#partidas ele jogou. Depois vai ler a quatidade de gols feitos em cada partida. No final, tudo isso será guardado em um
#dicionários, incluindo o total de gols feitos durante o campeonato.
jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(partidas):
    gols.append((int(input(f'->  Quantos gols na partida {c+1}? '))))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'o jogador {jogador["nome"]} jogou {partidas} partidas.')
for c in range(partidas):
        print(f'  => Na partida {c+1}, fez {jogador["gols"][c]}.')
print(f'Foi um total de {jogador["total"]} gols.')
