# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
a1 = int(input('Qual o primeiro termo da sua PA? '))
r = int(input('Qual a razão da sua PA? '))
for c in range(0, 10):
    print(a1 + (r * c))
