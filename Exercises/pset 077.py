'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

words = ('palavras', 'trabalho', 'acoradar', 'bone', 'perfume')

for p in words:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letter in p:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')
