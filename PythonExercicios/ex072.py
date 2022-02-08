#Crie um programa  que tenha um tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler o número pelo teclado(entre 0 e 20) e mostralo por extenso.
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove'
        , 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
        'vinte')
while True:
        num = int(input('Digite um número entre 0 é 20: '))
        if 0 <= num <= 20:
                print(f'Você digitou o número {cont[num]}.')
        resp = str(input('Você desaja continuar? [S/N]')).strip().upper()[0]
        if resp == 'N':
                break
print('Fim do programa.')