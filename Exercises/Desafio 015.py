# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantos KM foram rodados? '))
days = float(input('Quantos dias você ficou com o carro? '))
cost = (km * 0.15) + (days * 60)
print('O valor total a ser pago é de R${}' .format(cost))
