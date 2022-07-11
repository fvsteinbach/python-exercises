# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça digitação novamente até ter um valor correto.

gender = str(input('Qual o seu gênero0[M/F]? ')).strip().upper()

while gender != 'M' and gender != 'F':
    print('Não entendi! Você deve digitar apenas [M ou F]')
    gender = str(input('Qual o seu gênero? [M/F]? ')).strip().upper()
