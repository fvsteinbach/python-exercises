# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
l = float(input('Qual a largura em metros da sua parede? '))
h = float(input('Qual a altura em metros da sua parede? '))
a = l*h
tinta = a/2
print(f'Você vai precisa de {tinta} litros de tinta')
