# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que foram pares. Se o valor digitado for ímpar, desconsidere-o.
s = 0
for c in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s = s + n
print(f'A soma dos valores pares é {s}')
