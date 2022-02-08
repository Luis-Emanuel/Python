#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
num0 = int(input('Digite um número inteiro: '))
num1 = int(input('Digite outro número: '))
if num0 > num1:
    print('O primeiro número e maior.')
elif num0 < num1:
    print('O segundo número e maior.')
else :
    print('Não existe valores iguais.')