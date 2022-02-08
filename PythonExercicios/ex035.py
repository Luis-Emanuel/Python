#Desenvolva um programa que leia o comprimento de três retas e dica ao usuário se elas podem ou não formar um triângulo.
print('-=' * 15, '\nAnalisador de Triângulos\n', '-=' * 15)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos formão um triãngulo')
else:
    print('Os segmentos NÃO formão um triângulo')

