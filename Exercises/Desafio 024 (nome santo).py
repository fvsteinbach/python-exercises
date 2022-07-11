# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo".
city = str(input('Em que cidade você nasceu? ')).strip()
#city = city.lower()
# print(city.startswith('santo'))
print(city[:5].lower() == 'santo')
