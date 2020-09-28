'''Elabore um algoritmo que calcule o que deve ser pago considerando o preço normal da etiqueta e a escolha da condição
de pagamento. Ultize os codigos da tabela a seguir:

- a vista em dinheiro ou cheque: 10% de desconto
- a vista no cartão de crédito: 15% de desconto
- parcelado em 2x, preço normal da etiqueta sem juros
- parcelado em 2x, preço normal da etiqueta 10% de acrescimo '''

preco = float(input('Digite o valor do produto: R$ '))
modoPagamento = input("Digite a forma de pagamento: ")

dinheiroCheque = preco - (preco*10/100 )

if modoPagamento.lower() == 'Dinheiro'.lower() or modoPagamento.lower() == 'Cheque'.lower():
    print(f"Pagamento em {modoPagamento}")
    print(f'Pagamento em Dinheiro / Cheque 10% de Desconto: R$ {dinheiroCheque:.2f}')

elif modoPagamento.lower() == 'Cartão'.lower():
     cartao = preco - (preco * 15 /100)
     print(f'Pagamento em {modoPagamento}')
     print(f'Pagamento com Cartão, 15% de Desconto : R$ {cartao:.2f}')

elif modoPagamento.lower() == 'parcelado'.lower():
     print(f'Pagamento em 2x Preço da Etiqueta - R${preco:.2f}')

elif modoPagamento.lower() == 'credito'.lower():
     parcelado = preco + (preco * 15 /100)
     print(f'Pagamento {modoPagamento}')
     print(f'Pagamento em 2x Preço da Etiqueta , 15% de acrescimo R$ {parcelado:.2f}')

