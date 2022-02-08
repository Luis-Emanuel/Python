lar = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
are = lar*alt
tin = are/ 2
print('Sua parede tem uma dimensão  de {} x {} e sua área é de {}m².'.format(lar, alt, are))
print('Para pintar essa parede, você precisa de {}l de tinta'.format(tin))
