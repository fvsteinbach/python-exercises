# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode conprar considerando que US$1.00 = R$3.27.
wallet = float(input('Quantos reais você tem? '))
usd = wallet/3.27
print('Você pode comprar {:.2f} doláres' .format(usd))
