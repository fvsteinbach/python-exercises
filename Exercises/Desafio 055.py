# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
highest = 0
lowest = 0
for p in range(1, 6):
    weight = float(input(f'Qual o peso da {p}ª pessoa? '))
    if p == 1:
        highest = weight
        lowest = weight
    else:
        if weight > highest:
            highest = weight
        if weight < lowest:
            lowest = weight
print(f'O maior peso lido foi {highest}')
print(f'O menor peso lido foi {lowest}')
