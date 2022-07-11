# Faça um programa que leia três números e mostre qual é o maior e o menor.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

if n1 > n2 and n1 < n3:
    print(f'O maior número é {n1}')
if n2 > n1 and n2 > n3:
    print(f'O maior número é {n2}')
if n3 > n2 and n3 > n1:
    print(f'O maior número é: {n3}')
if n1 == n2 and n1 == n3:
    print(f'Os números são iguais')
if n1 < n2 and n1 < n3:
    print(f'O menor número é: {n1}')
if n2 < n3 and n2 < n1:
    print(f'O menor número é o {n2}')
if n3 < n1 and n3 < n2:
    print(f'O menor número é o {n3}')
