def leiaInteiro(numinteiro):
    while True:
        try:
            n = int(input(numinteiro))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: por favor digite um número INTEIRO valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[31mERRO: O usuário preferiu nao informar o valor\033[m')
            return 0
        else:
            return n
            break


def leiaReal(numreal):
    while True:
        try:
            n = float(input(numreal))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: por favor digite um número REAL valido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mERRO: O usuário não informou o valor\033[m')
            return 0
        else:
            return n


num = leiaInteiro('Digite um número inteiro: ')
num2 = leiaReal('Digite um número real: ')
print(f'O valor interiro digitado foi {num} e o real foi {num2}')
