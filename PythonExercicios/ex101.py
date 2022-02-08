#Crie um programa que tenha uma finção chamada voto() que vai receber como  parâmetro o ano de nascimento de uma
#pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleções.
def voto(idade):
    from datetime import date
    """
    Analisa a condição de voto
    :param valor: idade do usuario
    :return: Retorna a condição de voto
    """
    idade = date.today().year - ano
    if 18 <= idade < 70:
        return(f'Com {idade} anos:VOTO OBRIGATÓRIO')
    elif 16 < idade < 18 or idade > 70:
        return(f'Com {idade} anos:VOTO OPCIONAL')
    else:
        return(f'Com {idade} anos:NÃO VOTA')


ano = int(input('Em que ano você nasceu ? '))
print(voto(ano))
