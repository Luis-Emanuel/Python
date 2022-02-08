#Melhore o desafio 061, perguntando para o úsuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que mostrar 0 termos.
termo = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
mais = 10
c = 0
tot = 0
while mais != 0 :
    while c < mais:
        print('{} -> '.format(termo), end='')
        termo += r
        c+=1
        tot += 1
    print('PAUSA')
    c = 0
    mais = int(input('\nQuantos termos você quer a mais: '))
print('FIM')
print('progressão  finalizada com {} termos mostrados.'.format(tot))
