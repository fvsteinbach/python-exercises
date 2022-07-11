# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros.
m = float(input('Digite o valor em metros: '))
cm = m*100
mm = m*1000
print('O valor em metros é: {} \nO valor em milímetros é: {}' .format(cm, mm))
