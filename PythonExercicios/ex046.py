#Faça um programa qye mostre na tela uma contagem regressiva para o estouro de fogos de artificio. indo de 10
#até 0. com uma pausa de 1 segundo
from time import sleep
from datetime import date
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('FELIZ {}'.format(date.today().year))