# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('=' * 40)
print('Bem vindo ao mercadinho do Fernando')
print('=' * 40)
ttl = ttl_1k = lowest = c = 0
cheapest_name = ' '
while True:
    product_name = str(input('Qual o produto? ')).strip()
    product_price = int(input('Qual o valor do produto? '))
    c = c + 1
    ttl = ttl + product_price
    if product_price > 1000:
        ttl_1k = ttl_1k + 1
    if c == 1 or product_price < lowest:
        lowest = product_price
        cheapest_name = product_name
    cont = ' '
    while cont not in 'SN':
        cont = str(
            input('Deseja informar mais algum produto? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print(f'O valor total da compra é de R${ttl}.')
print(f'Foram inseridos {ttl_1k} produtos com valor maior que R$1.000,00')
print(f'O produto mais barato foi {cheapest_name} que custa R${lowest:.2f}')
