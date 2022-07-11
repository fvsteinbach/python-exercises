# Refaça o desafio 035 dos triângulos acrescentando o recurso de mostar que tipo de triângulo será formado
# - Equilatro: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

ab = int(input('Digite a medida da primeira reta: '))
cd = int(input('Digite a medida da segunda reta: '))
ef = int(input('Digite a medida da terceira reta: '))

if ab + cd > ef and cd + ef > ab and ef + ab > cd:
    print('O triângulo pode ser formado.')
    if ab == cd and cd == ef and ab == ef:
        print('Você formará um triângulo EQUILÁTERO.')
    elif ab != cd and cd != ef and ab != ef:
        print('Você formará um triângulo ESCALENO.')
    else:
        print('Você formará um triângulo ISÓSCELES.')
else:
    print('Você NÃO formará um triângulo.')
