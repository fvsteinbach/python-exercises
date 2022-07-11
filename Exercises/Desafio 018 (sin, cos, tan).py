# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians

x = float(input('Digite um ângulo qualquer: '))
sin = sin(radians(x))
cos = cos(radians(x))
tan = tan(radians(x))
print('O ângulo de {} tem seno de {:.2f}\nCosseno de {:.2f}\nE tangente de {:.2f}' .format(
    x, sin, cos, tan))
