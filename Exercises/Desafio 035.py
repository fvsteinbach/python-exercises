# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um trângulo.
ab = int(input('Digite a medida da primeira reta: '))
cd = int(input('Digite a medida da segunda reta: '))
ef = int(input('Digite a medida da terceira reta: '))

if ab + cd > ef and cd + ef > ab and ef + ab > cd:
    print('O triângulo pode ser formado.')
else:
    print('Não pode ser triângulo.')
