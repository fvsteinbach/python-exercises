# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# -A média de idade do grupo.
# -Qual é o nome do homem mais velho.
# -Quantas mulheres têm menos de 20 anos.
sum_age = 0
hm_age = 0
name_older_man = ''
totmulher20 = 0
for p in range(1, 5):
    name = str(input(f'Qual o nome da {p}ª pessoa? ')).strip()
    age = int(input(f'Qual a idade da {p}ª pessoa? '))
    gender = str(input(f'Qual gênero da {p}ª pessoa?[M/F] ')).strip().upper()
    sum_age = sum_age + age
    avg_age = sum_age / 4
    if p == 1 and gender == 'M':
        hm_age = age
        name_older_man = name
    if gender == 'M' and age > hm_age:
        hm_age = age
        name_older_man = name
    if gender == 'F' and age < 20:
        totmulher20 = totmulher20 + 1
print(f'A média de idade das 4 pessoas é de {avg_age} anos')
print(f'O homem mais velho tem {hm_age} anos e o nome dele é {name_older_man}')
print(f'São {totmulher20} mulheres com menos de 20 anos.')
