from ex115.lib.interface import *
from ex115.lib.arquivo import *
arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastra nova pessoa', 'Sair do Sistema'])
    if resp == 1:
        leiaArquivo(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resp == 3:
        cabecalho('>>> VOLTE SEMPRE! FIM <<<')
        break
    else:
        print('\033[31mERRO! Digite um opção valida.\033[m')
