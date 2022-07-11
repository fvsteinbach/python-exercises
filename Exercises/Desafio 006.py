# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raíz quadrada.

n = input('Digite um número: ')
d = float(n)*int(2)
t = float(n)*int(3)
r = float(n)**(1/2)
print('O dobro do seu núemro é: {}, o triplo é: {}, e a raíz quadrade é: {}' .format(d, t, r))
