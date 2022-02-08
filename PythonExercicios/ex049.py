#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolhes, só que agora utilizando um laço for
n = int(input('Qual  tabuada voçe deseja saber ?'))
print('-'*15)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, (n*c)))
