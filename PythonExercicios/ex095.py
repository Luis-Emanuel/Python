#Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo ummm sistema de visualição
#de detalhes do aproveitamento de cada jogador.
jogadores = list()
gol_por_partida = list()
jogador = dict()
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(partidas):
        gol_por_partida.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gol_por_partida'] = gol_por_partida[:]
    jogador['tot_gol'] = sum(jogador['gol_por_partida'])
    jogadores.append(jogador.copy())
    jogador.clear()
    gol_por_partida.clear()
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Escolha S ou N.')
    if resp == 'N':
        break
print('-='* 20)
print(f'{"cod":<2} {"nome":<10} {"gols":<10}  {"total":>}')
print('-'* 35)
for c, j in enumerate(jogadores):
    print(f'  {c:<2} {j["nome"]:<10}{str(j["gol_por_partida"]):<15} {j["tot_gol"]:>5}')
while True:
    print('-' * 35)
    cod = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if cod == 999:
        break
    elif cod > len(jogadores):
        print(f'ERRO! Não existe jogador com o código {cod}')
    else:
        print(f'--LEVANTAMENTO DO JOGGADOR {jogadores[cod]["nome"]}--')
        for i, v in enumerate(jogadores[cod]['gol_por_partida']):
            print(f'--> No jogo {i} fez {v} gols.')
        print('-' * 35)
print('<< VOLTTE SEMMPRE >>')