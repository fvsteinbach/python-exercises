# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
from turtle import clear


n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot = tot + 1
    else:
        print('\033[34m', end=' ')
    print(f'{c} ', end=' ')
print(f'\n\033 O número {n} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso é primo')
else:
    print('E por isso ele não é primo')
