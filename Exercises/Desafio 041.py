# A confederaçao nacional de natacao precisa de um progreama que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:

# - Até 9 anos: Mirim
# - Até 14 anos: Infantil
# - Até 19 anos: Junior
# - Até 20 anos: Sênior
# - Acima: Master
from datetime import date

year = int(input('Em que ano você nasceu? '))
hoje = date.today().year
age = hoje - year
if age <= 9:
    print(F'Uma vez que você têm {age} anos, você está na categoria: MIRIM.')
elif age > 9 and age <= 14:
    print(f'Uma vez que você têm {age} anos, você está na categoria: INFANTIL')
elif age > 14 and age <= 19:
    print(f'Uma vez que você têm {age} anos, você está na categoria: JÚNIOR')
elif age > 19 and age <= 20:
    print(f'Uma vez que você têm {age} anos, você está na categoria: SÊNIOR')
elif age > 20:
    print(f'Uma vez que você tem {age} anos, você está na categoria: MASTER')
