#Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhate á função input() do Python, só que
#que fazendo a validação para aceitar apenas um valor numérico.     EX:   n = leiaint('Digite um n')
def leiaInt(num):
    while True:
        val = input(num)
        if val.isnumeric():
            return val
            break
        else:
            print('\033[0;31mERRO! Digite um número valido.\033[m')


n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o número {n}')