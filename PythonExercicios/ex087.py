#Aprimore o desafio anterior, mostrando no final: A) A soma de todos valores pares digitados. B) A soma dos valores
#da terceira coluna. C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somac = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor da posição [{l}] [{c}]: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2 :
            somac += matriz[l][c]
        if l == 1:
            if matriz[l][c] >= maior:
                maior = matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^3} ]', end='')
    print('\n')
print('-=' * 30)
print(f'A soma dos valores pares é {soma}.')
print(f'A soma dos valores da terceira coluna é {somac}')
print(f'O maior valor da segunda linha é {maior}')
