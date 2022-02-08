#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
#mensagem com tamanho adaptável.
def txt(msg):
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))


txt('Oi')
txt('Como você está?')
txt('Obrigado!')