# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - A vista dinheiro/cheque:  10% de desconto
# - A vista no cartão: 5% de desconto
# - Em até 2x no cartão: Preço normal
# - 3x ou mais no cartão: 20% de juros
price = float(input('Qual o valor do produto? '))
payment = int(input("""Qual a forma de pagamento? Digite:
[1] para pagamento a vista no dinheiro/cheque com 10% de desconto.
[2] para pagamento a vista no cartão com 5% de desconto.
[3] para pagamento no cartão em até 2x. Preço normal.
[4] para pagamento no cartão em 3x ou mais com acréscimo de 20% sob o valor do produto.
"""))
while payment != 1 and payment != 2 and payment != 3 and payment != 4:
    print('Digite uma opção de pagamento válida.')
    payment = int(input("""Qual a forma de pagamento? Digite:
[1] para pagamento a vista no dinheiro/cheque com 10% de desconto.
[2] para pagamento a vista no cartão com 5% de desconto.
[3] para pagamento no cartão em até 2x. Preço normal.
[4] para pagamento no cartão em 3x ou mais com acréscimo de 20% sob o valor do produto.
"""))
if payment == 1:
    print(
        f'O valor total do produto com o desconto por pagamento a vista é de  R${price*0.9}')
elif payment == 2:
    print(
        f'O valor total do produto com o desconto para pagamento a vista no cartão é de R${price*0.95}')
elif payment == 3:
    print(
        f'O valor total do produto para pagamento em 2x no cartão é R${price} e ficará em duas parcelas iguais de R${price/2:.2f}')
elif payment == 4:
    split = int(input('Em quantas vezes você gostaria de parcelar? '))
    print(
        f'O valor total do produto para pagamento em 3x ou mais ficará R${price+(price * 0.2)} e serão {split} parcelas de R${(price + (price * 0.2)) / split}')
