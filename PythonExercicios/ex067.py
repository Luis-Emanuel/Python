#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interronpido quando o número solicitado for negativo.
c = 0
while True:
    print(30*'-')
    num = int(input('Quer ver a tabuada de qual valor ?'))
    print(30*'-')
    if num < 0:
        break
    for c in range(1,11):
        print(f'{num} X {c} = {num*c}')
print('FIM')