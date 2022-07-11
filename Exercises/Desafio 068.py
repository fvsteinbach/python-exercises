# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

while True:
    player_number = int(input('Digite seu número: '))
    pc_number = randint(0, 10)
    ttl = player_number + pc_number
    player_choice = ' '
    while player_choice not in 'PpIi':
        player_choice = str(
            input('Você escolhe Par ou Ímpar? ')).strip().upper()[0]
    if player_choice == 'P':
        if ttl % 2 == 0:
            print('Você ganhou!!')
        else:
            break
    if player_choice == 'I':
        if ttl % 2 > 0:
            print('Você ganhou!!')
        else:
            break
print(
    f'Você jogou {player_number} e o computador {pc_number} e o total foi {ttl}')
print('GAME OVER - Você perdeu')
