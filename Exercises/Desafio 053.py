# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

# Ex:
# Apos a sopa
# A sacada da casa
# A torre da derrota
# O lobo ama o bolo
# Anatoram a data da maratona

phrase = str(input('Digite a sua frase: ')).strip().upper()
split = phrase.split()
join = ''.join(split)
reverse = ''
for spell in range(len(join)-1, -1, -1):
    reverse = reverse + join[spell]
if reverse == join:
    print(f'O inverso de {phrase} é {reverse}')
    print('Portandno, sua frase é um palíndrono.')
else:
    print(f'O inverso de {phrase} é {reverse}')
    print('Portanto sua frase não é um palíndrono')
