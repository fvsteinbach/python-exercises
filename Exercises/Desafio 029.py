# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

speed = int(input('Em qual velocidade o carro estava? '))

if speed > 80:
    print(f'Você foi multado em: R${(speed-80)*7}')
else:
    print('Parabéns por andar abaixo do limite, você não foi multado.')
