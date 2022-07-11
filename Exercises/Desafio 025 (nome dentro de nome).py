# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
name = str(input('Qual seu nome completo? ')).strip()

if ('silva' in name.lower()) == True:
    print('Seu nome tem Silva')
else:
    print('Seu nome não tem Silva')
