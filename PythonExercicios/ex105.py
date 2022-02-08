#Faça um programa que tenha uma função notas() que pode receber varias notas de alunos e vai retornar um dicionário com
#seuintes informações:->Quantidade de notas  ->A maior nota  ->A menor nota  ->A média da turma  ->A situação (opcional)
#adicione também as docstrings.
def notas(*num, sit=False):
    """
    ->  Função para analisar notas e situação de aluno
    :param num: As notas do aluno.
    :param sit: (Parâmetro opcional) Ele indica se mostra ou não a situação do aluno
    :return: As informações do aluno dentro de um dicionario
    """
    ficha = dict()
    ficha['total'] = len(num)
    ficha['maior'] = max(num)
    ficha['menor'] = min(num)
    ficha['media'] = sum(num) / len(num)
    if sit == True:
        if ficha['media'] < 6:
            ficha['situação'] = 'RUIM'
        elif 6 < ficha['media'] <= 7:
            ficha['situação'] = 'RAZOÁVEL'
        else:
            ficha['situação'] = 'BOM'
    return ficha


resp = notas(5.5, 2.5, 10, 6.5)
print(resp)
help(notas)
