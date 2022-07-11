# Desenvolva um lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:

# -Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida
height = float(input('Qual sua altura em metros (utilize ".")? '))
weight = int(input('Qual o seu peso em KG? '))
imc = weight / (height * height)
if imc < 18.5:
    print(f'Cuidado! Seu IMC é de {imc:.2F} e você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print(
        f'PARABÉNS! Seu IMC foi de {imc:.2F} e você está dentro do peso ideal.')
elif imc >= 25 and imc < 30:
    print(
        f'CUIDADO! Seu IMC é de {imc:.2F} e você está com sobrepeso, sugiro começar uma dieta.')
elif imc >= 30 and imc < 40:
    print(
        f'MUITO CUIDADO! Seu IMC é de {imc:.2F} indicando que você está OBESO. Procure um médico.')
elif imc > 40:
    print(
        f'URGENTE!!!! Seu IMC é de {imc:.2F} indicando que você é está com OBESIDADE MÓRBIDA. Procure um médico IMEDIATAMENTE.')
