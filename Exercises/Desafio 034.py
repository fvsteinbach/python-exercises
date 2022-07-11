# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00 calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

income = int(input('Qual o seu salário? '))
if income <= 1250:
    print(
        f'O seu aumento vai ser de R${income*0.15}, totalizando um salário de R${(income*0.15)+income}')
else:
    print(
        f'O seu aumento vai ser de R${income*0.1}, totalizando um salário de R${(income*0.1)+income}')
