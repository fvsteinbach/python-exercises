# Crie um programa que leia dois valores e mostre um menu na tela:

# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
ops = int(input("""Selecione a operação desejada: 

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa

"""))
while ops != 5:
    if ops == 1:
        print(f'O resultado da soma dos seus valores é {n1+n2}')

        print(f'O resultado da multiplicação dos seus valores é {n1 * n2}')

    elif ops == 3:
        if n1 > n2:
            print(f'O maior valor é {n1}')
        elif n2 > n1:
            print(f'O maior valor é {n2}')
        else:
            print('Os valores são iguais')

    elif ops == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))

    elif ops == 5:
        print('Finalizando!')
