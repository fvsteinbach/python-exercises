# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com um desconto de 5%.
price = float(input('Qual o preço do produto? '))
desconto = price*0.05
descontado = price-desconto
print('O preço do produto com desconto é de {:.2f} reais, o desconto total foi de {:.2f} reais' .format(
    descontado, desconto))
