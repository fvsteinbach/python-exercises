# Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem:
# - O primeiro valor é o maoior
# - o Segundo valor é o maior
# - Não existe valor maior ambos sao iguais
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O primeiro número é o maior.')
elif n2 > n1:
    print('O segundo número é o maior.')
elif n2 == n1:
    print('Os números são iguais.')
