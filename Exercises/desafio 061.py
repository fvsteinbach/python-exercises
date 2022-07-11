# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura WHILE.
n1 = int(input('Digite o primeiro termo da sua PA: '))
r = int(input('Digite a razão da sua PA: '))
c = 0
while c < 10:
    pa = n1 + (r * c)
    c = c + 1
    print(f'O {c}ª termo é {pa}')
