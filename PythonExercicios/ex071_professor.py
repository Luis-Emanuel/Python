print(30*'=')
print('{:^30}'.format('BANCO DO BRASIL'))
print(30*'=')
num = int(input('Qual valor deseja ser sacado? '))
ced = 50
totc = 0
while True:
    if num >= ced:
        num -= ced
        totc += 1
    else:
        if totc > 0:
            print(f'Total de {totc} cédulas R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totc = 0
        if num == 0:
            break
print(30*'=')
print('Volte sempre ao BANCO DO BRASIL! Tenha um bom dia.')