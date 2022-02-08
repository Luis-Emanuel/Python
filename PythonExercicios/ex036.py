#Escreva um programa para aprovar o empréstimo bancario para a compra de uma casa. Pergunta o valor da casa, o salário do computador e em quantos anos ele vai pagar.
#A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.
casa: float = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador:'))
anos = int(input('Quantos anos?'))
prestacao = casa / (anos * 12)
m = salario * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {anos}  anos,  a prestação será de R${prestacao:.2f}')
if prestacao <= m:
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO')
