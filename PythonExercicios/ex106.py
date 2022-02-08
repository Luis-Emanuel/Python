#Faço um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
#Quando o usuário digitar a palavra 'FIM', o programa se encerrará. OBS:Use cores.
c = ('\033[m',        # 0 - sem cor
     '\033[0:0:41m',  # 1 - vermelho
     '\033[0:0:42m',  # 2 - verde
     '\033[0:0:44m',   # 3 - azul
     '\033[7;0m'     # 4 - branco
    )
def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 3)
    print(c[4])
    help(comando)
    print(c[0])

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor],end='')
    print('~' * tam)
    print(f'{msg:^30}')
    print('~' * tam)
    print(c[0],end='')
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca >'))
    if comando.strip().upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)