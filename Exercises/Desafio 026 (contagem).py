# Faça um programa que leia uma frase e mostre:
# - Quantas vezes aaprece a letra "A"
# - Em que posição ela aparece pela primeira vez:
# - Em que posição ela aparece a última vez:

phrase = str(input('Digite um frase: ')).strip().lower()
print(f'A letra A aparece {phrase.count("a")} vezes')
print(f'A letra A aparece pela primeira vez na posição {phrase.find("a")+1}')
print(f'A letra A aparece pela última vez na posição {phrase.rfind("a")+1}')
