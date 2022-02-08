def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'\003[0;31mERRO! \"{entrada}\" é um preço invalido!\033[m')
        else:
            valido = True
            return float(entrada)
