#Crie um programa onde 4 jogadores joguem um dado e tenham resultado aleatórios. Guarde esses resultados em um dicinário
#No inal, coloquee esses dicionários em ordem, sabendo quue o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
c = 1
jogo = { 'jogador_1': randint(1, 6),
         'jogador_2': randint(1, 6),
         'jogador_3': randint(1, 6),
         'jogador_4': randint(1, 6)}
ranking = dict()
print('-='*5, f'{"VALORES SORTEADOS":^5}', '-='*5)
for k, v in jogo.items():
    print(f'O {k} tirou o valor {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*6, f'{"RESULTADOS":^5}', '-='*6)
for k, v in enumerate(ranking):
    print(f'O {v[0]} ficou {k+1}° lugar e tirou {v[1]}')
    c+=1
print('-='*20)