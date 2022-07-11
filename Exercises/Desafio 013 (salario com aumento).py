# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
salary = float(input('Qual o seu salário? '))
sraise = salary*0.15
newsalary = sraise+salary
print('O valor do seu novo salário é de R${:.2f}, o aumento total foi de R${:.2f}' .format(
    newsalary, sraise))
