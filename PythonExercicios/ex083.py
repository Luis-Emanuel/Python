#Crie um progrma onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analizar
#se a expressão passada está com os parênteses abertos e fechada na ordem correta.
expr  = str(input('Escreva a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está valida !')
else:
    print('Sua expresssão está invalida')