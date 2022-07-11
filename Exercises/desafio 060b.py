fat = int(input('Digite um número qualquer: '))
for c in range(fat-1, 0, -1):
    fat = fat * c
print(f'O fatorial desse número é {fat}')
