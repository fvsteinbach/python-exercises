# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

n1 = input('Qual o nome do aluno 1? ')
n2 = input('Qual o nome do alunos 2? ')
n3 = input('Qual o nome do aluno 3? ')
n4 = input('Qual o nome do aluno 4? ')
ns = [n1, n2, n3, n4]
shuffle(ns)
print('A ordem de apresenteção deve ser a seguinte: {}' .format(ns))
