#Crie um programa onde o usúario possa digitar cinto valores númericos e cadastre-os em um lista, já na posição correta
#de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista  = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista ...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos}')
                break
            pos+=1
print('-='*10)
print(lista)
print('FIM')
