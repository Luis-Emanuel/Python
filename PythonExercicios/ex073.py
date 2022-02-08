#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação e depois mostre:
#a) Os 5 primeiros. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time do Flamengo.
time = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Red Bull Bragantino', 'Fluminense',
         'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico Paranaense',
         'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print('--'*100)
print(f'Listas de times do Brasileirão: {time}')
print('--'*100)
print(f'Os 5 primeiros são: {time[:5]}')
print('--'*100)
print(f'Os 4 últimos são: {time[-4:]}')
print('--'*100)
print(f'Times em ordem alfabética: {sorted(time)}')
print('--'*100)
print(f'O Flamengo está na {time.index("Flamengo") + 1} posição')
