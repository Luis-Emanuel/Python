#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
#A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os valores pares.
numeros = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')),
           int(input('Digite o terceiro número: ')), int(input('Digite o ultimo número: ')))
cont = 0
print(f'Você  digitou os valores :{numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 apareceu na posição {numeros.index(3)}')
else:
    print('O valor 3 não foi digitado.')
print(f'Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'{n} -> ', end='')
print('FIM')