# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Qual número você precisa saber a tabuada? '))
for c in range(1, 11):
    print(f'{n} x {c} = {n * c}')
