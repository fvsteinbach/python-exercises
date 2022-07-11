# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
n = (input('Digite um número; '))
ant = float(n)-int(1)
suc = float(n)+int(1)
print('O seu antecessor é {}, e o sucessor é {}.' .format(ant, suc))
