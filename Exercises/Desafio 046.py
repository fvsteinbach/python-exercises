# Faça um programa que mostre na tela uma contagram regressiva para o estourod e fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for c in range(10, -1, -1):
    sleep(1)
    print(c)
