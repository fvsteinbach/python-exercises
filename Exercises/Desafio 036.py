# Escreva um programa para aprovar um emprestimo bancario pra compra de uma casa. O programa vai perguntar o valor da casa, o salario de quem ta comprando, e em quantos anos ela vai comprar?
# Calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salário ou então o empréstimo será negado.

house_price = float(input('Qual o valor da casa? '))
buyer_income = float(input('Qual a sua renda média mensal? '))
years = int(input('Em quantos anos você quer pagar? '))
monthly_payment = house_price / (years*12)
if monthly_payment > (buyer_income * 0.3):
    print('Infelizmente o seu financiamento foi negado.')
elif monthly_payment < (buyer_income * 0.3):
    print(
        f'Parabéns! O seu financiamento foi pré-aprovado! O valor das parcelas será de R${monthly_payment:.2f} durante {years*12} meses.')
