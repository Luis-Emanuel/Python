#Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
#Á vista dinheiro/cheque: 10% de desconto           - Em até 2x no cartão:preço normal
#Á vista no cartão: 5% de desconto                  - 3x ou mais no cartão: 20% de juros
print(f'{"  LOJAS AMERICANS ":=^40}')
preco = float(input('reço das comppras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    novo = preco - (preco * 10/100)
elif opcao == 2:
    novo = preco - (preco * 5/100)
elif opcao == 3:
    novo = preco
    parcela = novo / 2
    print(f'O valor das parcelas será de {parcela:.2f} SEM JUROS')
elif opcao == 4:
    n_parcela = int(input('Quantas parcelas seram ?'))
    novo = preco + (preco * 20 / 100)
    parcela = novo / n_parcela
    print(f'O valor das parcelas será de {parcela:.2f} COM JUROS')
else:
    print('{:^40}'.format('xxx OPÇÃO_INVALIDA xxx'))
print(f'Sua compra de R${preco:.2f} vai custar R${novo:.2f} no final. ')