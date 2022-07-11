# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date
year = int(input('Digite um ano, digite 0 para verificar o ano atual: '))
if year == 0:
    year = date.today().year
if (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
    print('O ano é bissexto')
else:
    print('Não é bissexto')
