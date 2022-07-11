# Crie um programa que leia um número inteiro e mostre se ele é par ou impar

number = int(input('Digite um número: '))

odds = number % 2

if odds > 0:
    print('Seu número é impar')
else:
    print('Seu número é par')
