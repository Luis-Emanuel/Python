#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostra que tipo de triângulo será formado:
#-EQUILÁTERO: todos os lados iguais
#-ISÓSCELES: dois lados iguais
#-ESCALENO: todos os lados diferentes
r1 = int(input('Digite o primeiro segmento: '))
r2 = int(input('Digite o segundo segmsegundo: '))
r3 = int(input('Digite o terceiro segmterceiro: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Estas medidas podem formar um triângo')
    if r1 == r2 == r3:
        print('As retas formão um triângulo EQUILATERO')
    elif r1 != r2 != r3 != r1 :
        print('As retas formão um triângulo ESCALENO')
    else:
       print('As retas formão um triângulo ISÓSCELES')
else:
    print('Estas medidas NÃO podem formar um triângo')