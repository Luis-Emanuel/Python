#Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.
num = int(input('Digite um número? '))
print('O dobro de {} vale {} \nO triplo de {} vale {} \nA raiz quadrada de {} e igual a {:.2f}'.format(num,(num*2), num, (num*3), num, (num**(1/2))))
