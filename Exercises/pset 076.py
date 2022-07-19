'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

products_prices = ('pencil', 1.5, 
                  'notebook', 15.9,
                  'backpack', 100.23,
                  'pen', 2)

print('-' * 40)
print(f'{"PRICES":^40}')
print('-' * 40)
for pos in range(0, len(products_prices)):
    if pos % 2 == 0:
        print(f'{products_prices[pos]:.<30}', end='')
    else:
        print(f'R${products_prices[pos]:>7.2f}')
print('-' *40)
