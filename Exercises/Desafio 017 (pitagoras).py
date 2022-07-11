# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
# h² = ca² + co²
import math

ca = float(input('Qual a medida do cateto adjacente? '))
co = float(input('Qual a medida do cateto oposto? '))
hp = ca**2 + co**2
print('Considerando o Cateto Oposto como {}, e o cateto adjacente {}, aplicando o teorema de pitágoras a hipotenosa tem {}' .format(
    co, ca, math.sqrt(hp)))

'''
from math import hypot
ca = float(input('Qual a medida do cateto adjacente? '))
co = float(input('Qual a medida do cateto oposto? '))
hp = hypot(ca, co)
print('A hipotenusa é: {:.2f}' .format(hp))

'''
'''
ca = float(input('Qual a medida do cateto adjacente? '))
co = float(input('Qual a medida do cateto oposto? '))
hp = (ca**2 + co**2)**(1/2)
print('A hipotenusa é: {:.2f}' .format(hp))
'''
