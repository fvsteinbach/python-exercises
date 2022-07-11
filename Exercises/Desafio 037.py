# Escreva um programa que leia um numero inteiro qualquer e peça par o usuario escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 hexadecimal
number = int(input('Digite um número inteiro: '))
print(
    'Escolha a base de conversão:\n[1] Converter para binário \n[2] Converter para octal \n[3] Converter para hexadecimal')
option = int(input('Sua opção: '))
while option != 1 and option != 2 and option != 3:
    print('Opção inválida!')
    option = int(input('Digite sua opção novamente: '))
if option == 1:
    print(f'{number} convertido para binário é igual a {bin(number)[2:]}')
elif option == 2:
    print(f'{number} convertido para octal é {oct(number)[2:]}')
elif option == 3:
    print(f'{number} convertido para hexadecimal é {hex(number)[2:]}')
