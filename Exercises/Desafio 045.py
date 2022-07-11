# Crie um programa que faça o computador jogar jokenpô com você.
from random import choice
from time import sleep
game = str(input('Vamos jogar jokenpô? Sim ou não? ')).strip()

plays = ['pedra', 'papel', 'tesoura']

pc_choice = choice(plays)

if game.lower() == 'sim':
    jok = input('Você escolhe Pedra, Papel ou Tesoura? ')
    print(f'Eu escolho {pc_choice}')
    sleep(1)
    if jok.lower() == pc_choice:
        print('AFF! Deu empate. Vamos de novo! Aperte F5')
    elif jok.lower() == 'pedra' and pc_choice == 'papel':
        print('HAA! Eu ganhei! O papel abraça a pedra. Tente de novo newbie!')
        print('Aperte F5 para jogar novamente')
    elif jok.lower() == 'pedra' and pc_choice == 'tesoura':
        print('BLEH! Você ganhou na sorte!! Aperte F5 para jogar novamente.')
    elif jok.lower() == 'tesoura' and pc_choice == 'pedra':
        print('HAA!! Pedra quebra a tesoura. Você perdeu!!!')
        print('Aperte F5 para jogar novamente')
    elif jok.lower() == 'tesoura' and pc_choice == 'papel':
        print('URHG! Você ganhou... Tesoura corta o papel..')
        print('Quero revanche, aperte F5 e vamos de novo.')
    elif jok.lower() == 'papel' and pc_choice == 'tesoura':
        print('HELL YEAH! Eu ganhei! Tesoura corta o papel.')
        print('Quer perder de novo? Se sim aperte F5')
    elif jok.lower() == 'papel' and pc_choice == 'pedra':
        print('AFFF! Perdi de novo. Nada ver você ganhar porque o papel abraça a pedra...')
        print('Quero revanche, aperte F5 e vamos de novo!')
elif game.lower() == 'não' or game.lower() == 'nao':
    print('Okay, nem queria mesmo')
    sleep(2)
    print('Se mudar de ideia é só apertar F5')
