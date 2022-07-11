# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:

# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
from datetime import date

atual = date.today().year

age = int(input('Qual o seu ano de nascimento? '))
print(f'Quem nasceu em {age} tem {atual - age} anos em {atual}.')
alistamento = atual - age
if atual - age < 18:
    print('Você ainda não precisa se alistar.')
    print(f'Faltam {18 - alistamento} anos para o seu alistamento se tornar obrigatório. Ele deverá acontecer em: {atual + (18 - alistamento)}')
elif alistamento == 18:
    print('Você deve se alistar esse ano, fique atento as datas.')
elif alistamento > 18:
    print(
        f'Você deveria ter se alistado à {alistamento-18} anos atrás em {atual + (18 - alistamento)}. Caso não tenha se alistado, procure a junta militar o mais breve possível.')
