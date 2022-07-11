# Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um número de 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep

pc_number = randint(0, 10)

play = str(input(
    '============== GUESS THE NUMBER ============== Vamos jogar [Sim ou Não]? ')).strip().upper()

if play == 'SIM':
    choose = int(input('Vou pensar em um número de 0 a 10, tente adivinhar: '))
    print('Processando...')
    sleep(1)
    count = 0
    while choose != pc_number:
        choose = int(input(f'Você errou, tente novamente: '))
        count = count + 1
    if choose == pc_number:
        print(f'Parabéns você acertou o número! Você tentou {count} vezes.')

elif play == 'NÃO':
    print('BLEHH, Seu chato, nem queria jogar mesmo.')
