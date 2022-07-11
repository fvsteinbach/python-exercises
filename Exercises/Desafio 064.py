# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag).

soma = n = c = 0
n = int(input('Digite um número: ou [999] para parar. '))
while n != 999:
    soma = soma + n
    c = c + 1
    n = int(input('Digite um número: ou [999] para parar. '))
print(f'Foram inseridos {c} valores e a soma total é {soma}')
