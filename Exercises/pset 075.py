'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

user_num = (int(input('Digite um número: ')), int(input('Digite outro número número: ')), int(
    input('Digite mais um número: ')), int(input('Digite o último número: ')))

print(f'Seus números foram {user_num}')
print(f'O valor 9 apareceu {user_num.count(9)} vezes')
if 3 in user_num: 
  print(f'O 3 apareceu na {user_num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
print(f'Os valores pares foram: ')
for n in user_num:
    if n % 2 == 0:
        print(n, end=' ')
    