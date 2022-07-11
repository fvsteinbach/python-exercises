# Escreve um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuario descobrir qual foi o número escolhido pelo computador.

from random import sample
from time import sleep
numbers = [0, 1, 2, 3, 4, 5]
pc_number = sample(numbers, 1)
choose = int(input('Vou pensar em um número de 0 a 5, tente adivinhar: '))
print('Processando...')
sleep(2)
if choose == pc_number:
    print('Parabéns você acertou o número!')
else:
    print(f'Você errou, eu pensei em {pc_number},aperte F5 e tente novamente')
