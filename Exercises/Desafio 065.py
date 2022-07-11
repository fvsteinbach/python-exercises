# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar mais valores.

res = 'S'
avg = ttl = qnt = maior = menor = 0
while res in 'Ss':
    num = int(input('Digite um número: '))
    ttl = ttl + num
    qnt = qnt + 1
    if qnt >= 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    res = str(input('Quer continuar? [S/N] ')).upper().strip()
avg = ttl / qnt
print(f'Você digitou {qnt} números e a média foi {avg:.2f}.')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
