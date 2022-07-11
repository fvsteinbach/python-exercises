# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.

print('=' * 20)
print('REALIZE O CADASTRO')
print('=' * 20)
qnt_h = ttl_18 = qnt_f = 0
while True:
    age = int(input('Digite a idade: '))
    gender = ' '
    while gender not in 'MF':
        gender = str(input('Digite o gênero: [M/F] ')).strip().upper()[0]
    if age >= 18:
        ttl_18 = ttl_18 + 1
    if gender == 'M':
        qnt_h = qnt_h + 1
    if gender == 'F' and age < 20:
        qnt_f = qnt_f + 1
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print(f'Foram cadastradas {ttl_18} pessoas maiores de 18 anos.')
print(f'Foram cadastrados {qnt_h} homens.')
print(f'Foram cadastradas {qnt_f} mulheres com menos de 20 anos.')
