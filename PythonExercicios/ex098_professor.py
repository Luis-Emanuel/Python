#Faça um programa que tenha uma função chamada contador(), que receba três parâmettros; início, fim, passo. Seu programa
#tem realizar três contagens através da função criada:
#-->A)De 1 até 10, de 1 em 1             -->B)De 10 até 0, de 2 em 2                     -->C)Uma contagem personalizada
from time import sleep
def contador(ini, fim, pas):
    if pas < 0:
        pas *= -1
    if pas == 0:
        pas = 1
    print(f'Contagem de {ini} até {fim} de {pas} em {pas}')
    if ini < fim:
        cont = ini
        while cont <= fim:
            print(f'{cont} ', end='')
            cont += pas
            sleep(0.2)
    else:
        cont = ini
        while cont >= fim:
            print(f'{cont} ', end='')
            cont -= pas
            sleep(0.2)
    print('FIM')
    print('-=' * 30)


###############################
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('INÍCIO: '))
fim = int(input('FIM: '))
pas = int(input('PASSO: '))
contador(ini, fim, pas)
