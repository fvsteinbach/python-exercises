# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
#Primeiro: Ana
#Último: Souza

name = str(input('Qual o seu nome completo? ')).strip()
namelist = name.split()
print(f'Prazer em te conhecer {name} ...!')
print(f'Seu primeiro nome é {namelist[0]}')
print(f'Seu último nome é {namelist[len(namelist)-1]}')
