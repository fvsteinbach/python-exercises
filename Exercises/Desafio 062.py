# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
n1 = int(input('Digite o primeiro termo da sua PA: '))
r = int(input('Digite a razão da sua PA: '))
c = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c < total:
        pa = n1 + (r * c)
        c = c + 1
        print(f'O {c}ª termo é {pa}')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')
