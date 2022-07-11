# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

this_year = date.today().year
legal_age = 0
minor = 0
for c in range(1, 8):
    born = int(input(f'Qual o ano de nascimento da pessoas {c}? '))
    if this_year - born > 18:
        legal_age = legal_age + 1
    elif this_year - born < 18:
        minor = minor + 1
print(
    f'Das 7 pessoas, {minor} são menores de idade e {legal_age} são maiores.')
