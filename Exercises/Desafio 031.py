# Desenvolva um programa que pergunte a distnância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
trip = int(input('Qual a distância da sua viagem? '))
if trip <= 200:
    print(f'Sua passagem vai custar R${trip * 0.50}')
else:
    print(f'Sua passagem vai custar R${trip * 0.45}')
